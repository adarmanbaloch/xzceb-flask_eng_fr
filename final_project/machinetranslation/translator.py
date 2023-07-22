from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
  translator = MyMemoryTranslator()
  french_text = translator.translate(english_text, to_lang="fr")
  return french_text

def french_to_english(french_text):
  translator = MyMemoryTranslator()
  english_text = translator.translate(french_text, to_lang="en")
  return english_text
