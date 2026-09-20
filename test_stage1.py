"""Stage 1 v7: 20 required regressions plus offline invariant tests.

Uses fake models and temporary files only; never scans the Hub or runs Stage 2.
"""
import contextlib
import copy
import importlib.util
import io
import itertools
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('stage1', '01_collect_models.py')
stage1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stage1)


def model(model_id='org/model', languages=(), marker=False, downloads=500, **extra):
    return SimpleNamespace(id=model_id, languages=list(languages),
                           tags=['multilingual'] if marker else [], downloads=downloads, **extra)


def row(fake_model):
    return stage1.build_row(fake_model, stage1.classify_candidate(fake_model))


class OfflineTest(unittest.TestCase):
    def setUp(self):
        self.no_network = patch.object(stage1.api, 'list_models', side_effect=AssertionError('Network forbidden'))
        self.api_mock = self.no_network.start()
        self.addCleanup(self.no_network.stop)

    def tearDown(self):
        self.api_mock.assert_not_called()


class RequiredRegressions(OfflineTest):
    def test_18_exact_500_is_core(self):
        r = row(model(languages=['ko'], downloads=500))
        core, low, likely, fallback = stage1.partition_rows({r['model_id']: r})
        self.assertEqual((core, low, likely, fallback), ([r], [], [], []))
        self.assertEqual(r['popularity']['tier'], 'main')

    def test_19_exact_499_is_low(self):
        r = row(model(languages=['ko'], downloads=499))
        core, low, likely, fallback = stage1.partition_rows({r['model_id']: r})
        self.assertEqual((core, low, likely, fallback), ([], [r], [], []))
        self.assertEqual(r['popularity']['tier'], 'low_popularity')

    def test_20_popular_likely_never_core(self):
        r = row(model(languages=['en', 'fr'], marker=True, downloads=10_000_000))
        core, low, likely, fallback = stage1.partition_rows({r['model_id']: r})
        self.assertEqual((core, low, likely, fallback), ([], [], [r], []))
        self.assertEqual(r['candidate']['type'], 'multilingual_explicit')


CASES = [
    ('01_explicit', 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2', ['en','ja','ko'], False, 'A_verified', 'korean_explicit', 'explicit_language:korean'),
    ('02_explicit_wins', 'some-org/koelectra-ko-en', ['ko','en'], False, 'A_verified', 'korean_explicit', 'explicit_language:korean'),
    ('03_pair_ko_en', 'Helsinki-NLP/opus-mt-ko-en', [], False, 'A_verified', 'korean_translation_pair', 'translation_pair:ko-en'),
    ('04_pair_en_ko', 'Helsinki-NLP/opus-mt-en-ko', [], False, 'A_verified', 'korean_translation_pair', 'translation_pair:en-ko'),
    ('05_pair_ja_ko', 'some-org/translate-ja-ko', [], False, 'A_verified', 'korean_translation_pair', 'translation_pair:ja-ko'),
    ('06_koelectra', 'monologg/koelectra-base-v3-discriminator', [], False, 'A_verified', 'korean_name_strong', 'strong_korean_name:koelectra'),
    ('07_kobert', 'skt/kobert-base-v1', [], False, 'A_verified', 'korean_name_strong', 'strong_korean_name:kobert'),
    ('08_klue', 'hunkim/sentence-transformer-klue', [], False, 'A_verified', 'korean_name_strong', 'strong_korean_name:klue'),
    ('09_kokoro', 'hexgrad/Kokoro-82M', [], False, None, None, None),
    ('10_koala', 'some-org/koala-7b', [], False, None, None, None),
    ('11_token', 'some-org/token-classification-koala', [], False, None, None, None),
    ('12_multilingual_explicit', 'google-t5/t5-small', ['de','en','fr','ro'], True, 'B_likely', 'multilingual_explicit', 'multilingual_tag'),
    ('13_multilingual_marker', 'BAAI/bge-reranker-v2-m3', [], True, 'B_likely', 'multilingual_tag_only', 'multilingual_tag'),
    ('14_marker_one_language', 'org/model', ['en'], True, 'B_likely', 'multilingual_tag_only', 'multilingual_tag'),
    ('15_languages_without_marker', 'org/model', ['id','jv','su'], False, None, None, None),
    ('16_fallback', 'Qwen/Qwen3-8B', [], False, 'C_fallback', 'family_heuristic', 'family:qwen'),
    ('17_non_korean_blocks_fallback', 'Qwen/some-model', ['en','zh'], False, None, None, None),
]


def make_case(case):
    def test(self):
        _, mid, languages, marker, tier, kind, evidence = case
        result = stage1.classify_candidate(model(mid, languages, marker))
        if tier is None:
            self.assertIsNone(result)
        else:
            self.assertEqual((result['tier'], result['type']), (tier, kind))
            self.assertEqual(result['confidence'], {'A_verified':'high', 'B_likely':'medium', 'C_fallback':'low'}[tier])
            self.assertIn(evidence, result['evidence'])
            self.assertIn(kind, stage1.CANDIDATE_TYPES[tier])
    return test


for case in CASES:
    setattr(RequiredRegressions, 'test_' + case[0], make_case(case))


class InvariantRegressions(OfflineTest):
    def test_structured_sources_aliases_and_markers(self):
        for alias in ('ko','kor','korean','ko-kr','language:ko','language:kor','language:korean','language:ko-kr','KO_KR'):
            for source in ('tags','language','languages','card_data','cardData'):
                fake = SimpleNamespace(id='org/model', **{source: {'language':[alias]} if source in ('card_data','cardData') else [alias]})
                with self.subTest(alias=alias, source=source):
                    self.assertEqual(stage1.classify_candidate(fake)['type'], 'korean_explicit')
        for tag in ('ko-model', 'ko-sbert', 'koelectra', 'en-model', 'tokenizer'):
            self.assertIsNone(stage1.classify_candidate(SimpleNamespace(id='org/model', tags=[tag])))
        for marker in stage1.MULTILINGUAL_MARKERS:
            fake = SimpleNamespace(id='org/model', card_data={'language':['en','en-US','language:'+marker]})
            result = stage1.classify_candidate(fake)
            self.assertEqual(result['type'], 'multilingual_tag_only')
            self.assertEqual(result['languages'], ['en'])
            self.assertEqual(result['concrete_language_count'], 1)

    def test_translation_and_strong_name_boundaries(self):
        for name, pair in [('ko_zh_translation','ko-zh'),('translation-ko-ja','ko-ja'),('translation.ja.ko','ja-ko'),('translation/ko/en','ko-en')]:
            self.assertIn(pair, stage1.detect_korean_translation_pair('org/'+name))
        for name in ('ko-model','kor-model','tokenizer','kokoro','unknown-model','koala-model','kosmos-model','ko-english','en-korean','ko-zz','ko-enough','xko-en','ko-ko'):
            self.assertEqual(stage1.detect_korean_translation_pair('org/'+name), [])
            self.assertEqual(stage1.detect_strong_korean_name('org/'+name), [])
            self.assertEqual(stage1.classify_candidate(model('org/'+name, ['ko']))['type'], 'korean_explicit')
        for name in stage1.STRONG_KOREAN_NAMES:
            self.assertIn(name, stage1.detect_strong_korean_name('org/'+name+'-base'))
        for mid in ('en/ko-model','kobert/ordinary-model'):
            self.assertIsNone(stage1.classify_candidate(model(mid)))
        self.assertEqual(stage1.classify_candidate(model('org/koelectra-ko-en'))['type'], 'korean_translation_pair')

    def test_korean_explicit_flag_is_metadata_only(self):
        for mid, kind in [('org/translation-ko-en','korean_translation_pair'),('org/ko-sbert','korean_name_strong')]:
            r = row(model(mid))
            self.assertEqual(r['candidate']['type'], kind)
            self.assertFalse(r['language']['korean_explicit'])
            self.assertEqual(r['language']['languages'], [])
        self.assertTrue(row(model('org/kobert',['ko']))['language']['korean_explicit'])

    def test_all_partitions_and_unknown_types(self):
        models = {}
        for mid, langs, marker in [('org/kobert',[],False),('org/multi',[],True),('org/Qwen',[],False)]:
            for downloads in (79,80,499,500,501):
                r = row(model(f'{mid}-{downloads}',langs,marker,downloads))
                models[r['model_id']] = r
        partitions = stage1.partition_rows(models)
        self.assertEqual([len(rows) for rows in partitions], [2,2,4,4])
        for invalid in ('multilingual_explicit','multilingual_tag_only','family_heuristic','unknown','korean_name'):
            r = row(model(languages=['ko']))
            r['candidate']['type'] = invalid
            with self.assertRaises(ValueError):
                stage1.partition_rows({r['model_id']:r})

    def test_same_tier_merge_priority_and_evidence(self):
        mid = 'org/koelectra-ko-en'
        types = [('korean_name_strong','strong_korean_name:koelectra',[]),
                 ('korean_translation_pair','translation_pair:ko-en',[]),
                 ('korean_explicit','explicit_language:korean',['ko'])]
        for order in itertools.permutations(types):
            models = {}
            for kind, evidence, languages in order:
                fake = model(mid,languages)
                classification = stage1.classify_candidate(fake)
                classification.update(type=kind,evidence=[evidence])
                stage1.merge_candidate(models,fake,kind,classification)
            self.assertEqual(len(models),1)
            r = models[mid]
            self.assertEqual(r['candidate']['type'],'korean_explicit')
            self.assertEqual(set(r['candidate']['evidence']),{item[1] for item in types})
            self.assertEqual(len(r['matched_tasks']),3)
        for observations in ([[],['en','fr']], [['en','fr'],[]]):
            models = {}
            for languages in observations:
                fake = model('org/multi',languages,True)
                stage1.merge_candidate(models,fake,'task',stage1.classify_candidate(fake))
            self.assertEqual(models['org/multi']['candidate']['type'],'multilingual_explicit')
            self.assertEqual(models['org/multi']['matched_tasks'],['task'])

    def fixture(self, directory):
        outputs = ('CORE_OUTPUT','LOW_POPULARITY_OUTPUT','LIKELY_OUTPUT','FALLBACK_OUTPUT','GROUP_OUTPUT','STATE_OUTPUT')
        settings = {name:Path(directory)/getattr(stage1,name).name for name in outputs}
        settings['DATA_DIR'] = Path(directory)
        models = {}
        for downloads in (500,499):
            for name, languages in [('explicit',['ko']),('translation-ko-en',[]),('kobert',[])]:
                r = row(model(f'org/{name}-{downloads}',languages,downloads=downloads))
                models[r['model_id']] = r
        for fake in (model('org/multi',['en','fr'],True),model('org/marker',[],True),model('org/Qwen')):
            r = row(fake); models[r['model_id']] = r
        # Structured Model Card marker is absent from raw Hub tags.
        card = SimpleNamespace(id='org/card-only',tags=[],card_data={'language':['multilingual']},downloads=80)
        r = row(card);models[r['model_id']] = r
        state={'stage1_version':7,'config':{'min_downloads':80,'core_downloads':500,'core_downloads_inclusive':True,'core_candidate_tier':'A_verified'},'completed_tasks':list(stage1.TASKS),'task_stats':{task:{'error':None} for task in stage1.TASKS}}
        return settings,models,state

    def test_output_audit_and_group_union(self):
        with tempfile.TemporaryDirectory() as directory:
            settings,models,state=self.fixture(directory)
            with patch.multiple(stage1,**settings):
                stage1.save_all(models,state)
                counts=stage1.validate_outputs()
                self.assertEqual(counts[stage1.CORE_OUTPUT.name],3)
                self.assertEqual(counts[stage1.LOW_POPULARITY_OUTPUT.name],3)
                groups=stage1.build_groups(models)
                self.assertEqual(sum(g['member_count'] for g in groups),len(models))
                self.assertEqual({v['model_id'] for g in groups for v in g['variants']},set(models))

    def test_audit_rejects_contamination_duplicates_and_bad_groups(self):
        with tempfile.TemporaryDirectory() as directory:
            settings,models,state=self.fixture(directory)
            with patch.multiple(stage1,**settings), contextlib.redirect_stdout(io.StringIO()):
                for path_name in ('CORE_OUTPUT','LOW_POPULARITY_OUTPUT'):
                    for bad_type in ('multilingual_explicit','multilingual_tag_only','family_heuristic','unknown'):
                        stage1.save_all(models,state)
                        path=getattr(stage1,path_name)
                        rows=[json.loads(line) for line in path.read_text().splitlines()]
                        rows[0]['candidate']['type']=bad_type
                        stage1.save_jsonl_atomic(rows,path)
                        with self.assertRaises(AssertionError): stage1.validate_outputs()
                stage1.save_all(models,state)
                rows=[json.loads(line) for line in stage1.CORE_OUTPUT.read_text().splitlines()]
                stage1.save_jsonl_atomic(rows+rows[:1],stage1.CORE_OUTPUT)
                with self.assertRaisesRegex(AssertionError,'Duplicate'): stage1.validate_outputs()
                stage1.save_all(models,state)
                stage1.save_jsonl_atomic([],stage1.GROUP_OUTPUT)
                with self.assertRaisesRegex(AssertionError,'Groups differ'): stage1.validate_outputs()

    def test_checkpoint_version_and_publishing_without_scan(self):
        with tempfile.TemporaryDirectory() as directory:
            settings,models,state=self.fixture(directory)
            def fake_main():
                self.assertEqual(stage1.CORE_OUTPUT.parent,Path(directory)/'.stage1_v7_checkpoint')
                stage1.save_all(models,state)
            with patch.multiple(stage1,**settings), patch.object(stage1,'main',fake_main), contextlib.redirect_stdout(io.StringIO()):
                stage1.run_collection()
                self.assertTrue(stage1.CORE_OUTPUT.exists())
                self.assertEqual(json.loads(stage1.STATE_OUTPUT.read_text())['stage1_version'],7)
                stage1.validate_outputs()


if __name__ == '__main__':
    unittest.main()
