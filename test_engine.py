import copy
import json
import unittest
from pathlib import Path
from engine import analyze
EXAMPLE=json.loads(Path(__file__).with_name("example.json").read_text())

class Tests(unittest.TestCase):
    def test_perfect(self):
        r=analyze({'rows':[{'confidence':1,'correct':True},{'confidence':0,'correct':False}]})
        self.assertEqual(r['brier'],0)
        self.assertEqual(r['ece'],0)
    def test_ties(self):
        r=analyze({'rows':[{'confidence':.5,'correct':True},{'confidence':.5,'correct':False}]})
        self.assertEqual(r['risk_coverage'],[{'threshold':.5,'coverage':1,'risk':.5}])
        self.assertEqual(r['brier'],.25)
    def test_nan(self):
        with self.assertRaises(ValueError): analyze({'rows':[{'confidence':float('nan'),'correct':True}]})
    def test_empty(self):
        with self.assertRaises(ValueError): analyze({'rows':[]})

if __name__=="__main__": unittest.main()
