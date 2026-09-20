"""Offline classification regressions and corpus boundaries for Stage 1 v4."""
import importlib.util
import unittest
import contextlib
import io
import json
import tempfile
from pathlib import Path
from unittest.mock import patch
from types import SimpleNamespace

spec = importlib.util.spec_from_file_location("stage1", "01_collect_models.py")
stage1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stage1)


class ClassificationTests(unittest.TestCase):
    def test_required_regressions(self):
        cases = [
            ("some-org/model", ["ko"], [], "A_verified", "korean_explicit"),
            ("some-org/ko-model", [], [], "A_verified", "korean_name"),
            ("some-org/koelectra-base", [], [], "A_verified", "korean_name"),
            ("some-org/model", ["en"], ["multilingual"], "B_likely", "multilingual_tag_only"),
            ("some-org/model", ["en", "fr"], [], "B_likely", "bilingual_language_list"),
            ("some-org/model", ["en", "fr", "de"], [], "A_verified", "multilingual_language_list"),
            ("some-org/model", ["ko", "en"], [], "A_verified", "korean_explicit"),
            ("some-org/Gemma", ["en"], ["multilingual"], "B_likely", "multilingual_tag_only"),
            ("some-org/Gemma", ["en"], [], None, None),
            ("HauhauCS/Gemma-4-E4B-Uncensored-HauhauCS-Aggressive", ["en"], ["multilingual"], "B_likely", "multilingual_tag_only"),
            ("some-org/model", ["en", "fr"], ["multilingual"], "A_verified", "multilingual_explicit"),
            ("some-org/Gemma", [], [], "C_fallback", "family_heuristic"),
            ("some-org/ko-model", ["en", "fr", "de"], ["multilingual"], "A_verified", "korean_name"),
        ]
        for model_id, languages, tags, tier, kind in cases:
            with self.subTest(model_id=model_id, languages=languages, tags=tags):
                result = stage1.classify_candidate(SimpleNamespace(id=model_id, languages=languages, tags=tags))
                if tier is None:
                    self.assertIsNone(result)
                else:
                    self.assertEqual((result["tier"], result["type"]), (tier, kind))
                    self.assertEqual(result["confidence"], {"A_verified": "high", "B_likely": "medium", "C_fallback": "low"}[tier])

    def test_normalization_and_name_boundaries(self):
        for alias in ("ko", "kor", "korean", "ko-kr", "KO_KR", "language:kor"):
            result = stage1.classify_candidate(SimpleNamespace(id="org/model", tags=[alias]))
            self.assertEqual(result["type"], "korean_explicit")
        for marker in ("multilingual", "multilinguality", "multi-lingual", "multi-language", "language:multi-language"):
            result = stage1.classify_candidate(SimpleNamespace(id="org/model", tags=["en", "en-US", marker]))
            self.assertEqual(result["type"], "multilingual_tag_only")
            self.assertEqual(result["concrete_language_count"], 1)
            result = stage1.classify_candidate(SimpleNamespace(id="org/model", tags=[marker]))
            self.assertEqual(result["tier"], "B_likely")
        for name in ("token", "kokoro", "unknown", "notkorean", "xkobert", "koreanized"):
            self.assertFalse(stage1.is_korean_model_name("org/" + name))
        for name in ("ko", "kor", "korean", "ko-kr", "kobert", "kogpt2", "kosimcse-base", "korbert", "korean-llama"):
            self.assertTrue(stage1.is_korean_model_name("org/" + name))
        result = stage1.classify_candidate(SimpleNamespace(id="org/model", tags=[], card_data={"language": ["en", "fr", "de"]}))
        self.assertEqual(result["tier"], "A_verified")

    def test_partition_boundaries_and_group_union(self):
        models = {}
        for tier in ("A_verified", "B_likely", "C_fallback"):
            for downloads in (99, 100, 499, 500):
                model_id = f"org/{tier}-{downloads}"
                model = SimpleNamespace(id=model_id, tags=[], downloads=downloads)
                classification = dict(tier=tier, type="fixture", confidence="high", languages=[], multilingual_marker=False, evidence=[])
                models[model_id] = stage1.build_row(model, classification)
                self.assertEqual(models[model_id]["stage"]["stage1_version"], 4)
        partitions = stage1.partition_rows(models)
        self.assertEqual([len(rows) for rows in partitions], [1, 2, 3, 3])
        retained = {row["model_id"]: row for rows in partitions for row in rows}
        groups = stage1.build_groups(retained)
        self.assertEqual(sum(group["member_count"] for group in groups), 9)
        self.assertEqual({variant["model_id"] for group in groups for variant in group["variants"]}, set(retained))


class CollectionTests(unittest.TestCase):
    def test_complete_collection_and_failed_scan_preserves_outputs(self):
        class API:
            def list_models(self, **kwargs):
                assert kwargs["limit"] is None
                return iter([
                    SimpleNamespace(id="org/ko-model", tags=["ko"], downloads=500),
                    SimpleNamespace(id="org/weak", tags=["en", "multilingual"], downloads=100),
                    *[SimpleNamespace(id=f"org/low-{i}", tags=["ko"], downloads=99) for i in range(10)],
                ])
        names = ("CORE_OUTPUT", "LOW_POPULARITY_OUTPUT", "LIKELY_OUTPUT", "FALLBACK_OUTPUT", "GROUP_OUTPUT", "STATE_OUTPUT")
        with tempfile.TemporaryDirectory() as directory:
            values = {name: Path(directory) / getattr(stage1, name).name for name in names}
            values.update(DATA_DIR=Path(directory), TASK_SLEEP_SECONDS=0, api=API())
            with patch.multiple(stage1, **values), contextlib.redirect_stdout(io.StringIO()):
                stage1.run_collection()
                counts = stage1.validate_outputs()
                self.assertEqual(counts[stage1.CORE_OUTPUT.name], 1)
                self.assertEqual(counts[stage1.LIKELY_OUTPUT.name], 1)
                state = json.loads(stage1.STATE_OUTPUT.read_text())
                for stats in state["task_stats"].values():
                    self.assertEqual(stats["scanned"], 12)
                    self.assertEqual(stats["retained"], 2)
                    self.assertEqual(stats["cutoff_downloads"], 99)
                    self.assertTrue(stats["cutoff_reached"])
                before = {name: getattr(stage1, name).read_bytes() for name in names}
                with patch.object(stage1.api, "list_models", side_effect=ConnectionError("offline")):
                    with self.assertRaises(AssertionError):
                        stage1.run_collection()
                self.assertEqual(before, {name: getattr(stage1, name).read_bytes() for name in names})


if __name__ == "__main__":
    unittest.main()
