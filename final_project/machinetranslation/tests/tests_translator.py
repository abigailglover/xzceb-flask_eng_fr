import unittest
from translator import english_to_french, french_to_english
class TestEngToFr(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("How are you?"), "Comment es-tu?")
        self.assertEqual(english_to_french("I like the colour red."), "J'aime la couleur rouge.")
        self.assertEqual(english_to_french(""), "Method failed with status code 400: Unable to validate payload size, the 'text' is empty.")
        self.assertNotEqual(english_to_french(""), "")

class TestFrToEng(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Comment es-tu?"), "How are you?")
        self.assertEqual(french_to_english("Quel âge as-tu?"), "How old are you?")
        self.assertEqual(french_to_english(""), "Method failed with status code 400: Unable to validate payload size, the 'text' is empty.")
        self.assertNotEqual(french_to_english(""), "")

unittest.main()
