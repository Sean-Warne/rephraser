import unittest
import rephraser

class test_rephraser(unittest.TestCase):
    def test_rephrase_string(self):
        rephrased_str = rephraser.rephrase_string('Happy cat')
        print(rephrased_str)
        self.assertEqual(type(rephrased_str), type('Happy cat'))