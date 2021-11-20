import unittest
import rephraser

class test_rephraser(unittest.TestCase):
    def test_rephrase_string(self):
        phrase = "don't touch me"
        rephrased_str = rephraser.rephrase_string(phrase)
        print(rephrased_str)
        self.assertEqual(type(rephrased_str), type(phrase))