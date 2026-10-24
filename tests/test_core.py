import unittest,itertools,math
from sequential_evalue_ledger import run
class Tests(unittest.TestCase):
 def test_uniform_beta_all_success_closed_form(self):
  r=run({'events':[1]*10,'null_probability':.5})
  for step in r['steps']:self.assertAlmostEqual(step['e_value'],2**step['n']/(step['n']+1),places=8)
  self.assertEqual(r['first_threshold_crossing'],8)
 def test_exact_null_expectation_over_all_six_step_sequences(self):
  values=[run({'events':list(events)})['steps'][-1]['e_value']for events in itertools.product((0,1),repeat=6)];self.assertAlmostEqual(sum(values)/64,1)
 def test_first_crossing_not_erased_when_later_evalue_falls(self):
  r=run({'events':[1]*8+[0]*8});self.assertEqual(r['first_threshold_crossing'],8);self.assertFalse(r['steps'][-1]['crossed_threshold'])
 def test_empty_sequence_and_bool_rejection(self):
  self.assertIsNone(run({'events':[]})['first_threshold_crossing'])
  with self.assertRaises(ValueError):run({'events':[True]})
