"""Offline Stage 1 v7 / Stage 2 v6 compatibility checks."""
import copy
import importlib.util
import unittest

spec = importlib.util.spec_from_file_location('stage2', '02_enrich_metadata.py')
stage2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stage2)


class CompatibilityTests(unittest.TestCase):
    def make_row(self, pool, downloads, kind):
        row = {key: {} for key in ('author','task','family','stage1_quality','model',
               'quantization','artifacts','hardware','license','base_models','datasets','metrics')}
        row.update(model_id='org/model',candidate={'tier':'A_verified','type':kind},
                   popularity={'stage1':{'downloads':downloads},'current':{'downloads':1}},
                   language={'stage1':{'languages':[],'korean_explicit':False}},
                   source={'readme':{'available':False}},stage={
                       'source_pool':pool,'source_stage1_version':7,'stage2_version':6,
                       'metadata_enriched':True,'semantic_enriched':False})
        return row

    def test_all_types_and_boundaries(self):
        for kind in stage2.A_VERIFIED_TYPES:
            for pool, downloads, valid in [('core',500,True),('core',499,False),
                                          ('low_popularity',80,True),('low_popularity',499,True),
                                          ('low_popularity',79,False),('low_popularity',500,False)]:
                with self.subTest(kind=kind,pool=pool,downloads=downloads):
                    row=self.make_row(pool,downloads,kind)
                    if valid:
                        self.assertEqual(stage2.validate_stage2_rows([row],pool)['bad_count'],0)
                    else:
                        with self.assertRaises(ValueError):stage2.validate_stage2_rows([row],pool)

    def test_old_or_non_korean_type_rejected(self):
        for kind in ('korean_name','multilingual_explicit','multilingual_tag_only','family_heuristic'):
            with self.assertRaises(ValueError):
                stage2.validate_stage2_rows([self.make_row('core',500,kind)],'core')
        row=self.make_row('core',500,'korean_explicit')
        row['stage']['source_stage1_version']=6
        with self.assertRaises(ValueError):stage2.validate_stage2_rows([row],'core')

    def test_language_evidence_preserves_metadata(self):
        for kind in stage2.A_VERIFIED_TYPES:
            source={'candidate':{'tier':'A_verified','type':kind,'evidence':['fixture']},
                    'language':{'languages':['ko'] if kind=='korean_explicit' else [],
                                'korean_explicit':kind=='korean_explicit'}}
            original=copy.deepcopy(source)
            language=stage2.verify_languages(source,{},None)
            self.assertTrue(language['korean']['verified'])
            self.assertIn('stage1:'+kind,language['korean']['evidence'])
            self.assertEqual(language['stage1'],original['language'])
            self.assertEqual(source,original)

    def test_old_stage2_version_does_not_resume(self):
        row=self.make_row('core',500,'korean_explicit')
        row['stage']['stage2_version']=5
        self.assertFalse(stage2.resume_matches(row,{'stage':{'stage1_version':7}},'core'))


if __name__=='__main__':
    unittest.main()
