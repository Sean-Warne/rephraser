import unittest
import rephraser

class test_rephraser(unittest.TestCase):
    def test_rephrase_string(self):
        phrase = "happy cat"
        rephrased_str = rephraser.rephrase_string(in_str=phrase, out_style='username')
        print(rephrased_str)
        self.assertEqual(type(rephrased_str), type(phrase))