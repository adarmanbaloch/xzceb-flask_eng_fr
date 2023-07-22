import unittest
from translator import english_to_french, french_to_english

class TestTranslations(unittest.TestCase):

    def test_english_to_french(self):
        """
        Test the English to French translation.
        """
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_french_to_english(self):
        """
        Test the French to English translation.
        """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == "__main__":
    unittest.main()
