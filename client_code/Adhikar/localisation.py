# ------------------------------------------------------
# Adhikar App — localization.py
# Multi-language support for UI and legal answers
# ------------------------------------------------------

# Supported languages: English (en), Hindi (hi), Tamil (ta)

# ------------------------------------------------------
# Translation Dictionary
# ------------------------------------------------------

TRANSLATIONS = {
  "en": {
    "app_title": "Adhikar",
    "tagline": "Personalized Justice for Every Citizen",
    "get_started": "Get Started",
    "enter_question": "Type your legal question here...",
    "submit": "Submit",
    "loading": "Thinking...",
    "ask_another": "Ask Another Question",
    "about_title": "About Adhikar",
    "mission": "Empowering every citizen with legal awareness.",
    "disclaimer": "Disclaimer: This is an AI-powered legal literacy tool and not official legal advice.",
    "contact": "Contact us at adhikar@support.in",
    "no_answer": "Sorry, I don’t have an answer yet.",
    "recommended_schemes": "Recommended Welfare Schemes",
    "related_laws": "Relevant Laws",
    "official_links": "Official Resources"
  },

  "hi": {
    "app_title": "अधिकार",
    "tagline": "हर नागरिक के लिए व्यक्तिगत न्याय",
    "get_started": "शुरू करें",
    "enter_question": "अपना कानूनी प्रश्न यहाँ लिखें...",
    "submit": "भेजें",
    "loading": "सोच रहा हूँ...",
    "ask_another": "एक और प्रश्न पूछें",
    "about_title": "अधिकार के बारे में",
    "mission": "हर नागरिक को कानूनी जागरूकता के माध्यम से सशक्त बनाना।",
    "disclaimer": "अस्वीकरण: यह एक एआई आधारित कानूनी जानकारी उपकरण है, आधिकारिक कानूनी सलाह नहीं।",
    "contact": "हमसे संपर्क करें: adhikar@support.in",
    "no_answer": "क्षमा करें, इस प्रश्न का उत्तर फिलहाल उपलब्ध नहीं है।",
    "recommended_schemes": "सुझाए गए सरकारी योजनाएँ",
    "related_laws": "संबंधित कानून",
    "official_links": "आधिकारिक स्रोत"
  },

  "ta": {
    "app_title": "அதிகார்",
    "tagline": "ஒவ்வொரு குடிமகனுக்கும் தனிப்பட்ட நீதிகல்",
    "get_started": "தொடங்குங்கள்",
    "enter_question": "உங்கள் சட்ட கேள்வியை இங்கே தட்டச்சு செய்யுங்கள்...",
    "submit": "சமர்ப்பிக்கவும்",
    "loading": "யோசித்து கொண்டிருக்கிறேன்...",
    "ask_another": "மற்றொரு கேள்வி கேளுங்கள்",
    "about_title": "அதிகார் பற்றி",
    "mission": "ஒவ்வொரு குடிமகனையும் சட்ட விழிப்புணர்வுடன் அதிகாரமளித்தல்.",
    "disclaimer": "குறிப்பு: இது ஒரு செயற்கை நுண்ணறிவு சட்ட விழிப்புணர்வு கருவி, இது அதிகாரபூர்வ சட்ட ஆலோசனை அல்ல.",
    "contact": "எங்களை தொடர்பு கொள்ளுங்கள்: adhikar@support.in",
    "no_answer": "மன்னிக்கவும், இந்த கேள்விக்கு பதில் இன்னும் இல்லை.",
    "recommended_schemes": "பரிந்துரைக்கப்பட்ட நலத் திட்டங்கள்",
    "related_laws": "தொடர்புடைய சட்டங்கள்",
    "official_links": "அதிகாரப்பூர்வ ஆதாரங்கள்"
  }
}


# ------------------------------------------------------
# Utility Functions
# ------------------------------------------------------

DEFAULT_LANGUAGE = "en"


def translate(key, lang=DEFAULT_LANGUAGE):
  """
    Translate a given key into the target language.
    Fallback to English if key or language is missing.
    """
  if lang not in TRANSLATIONS:
    lang = DEFAULT_LANGUAGE

  translation = TRANSLATIONS[lang].get(key)

  if translation is None:
    # fallback gracefully to English
    translation = TRANSLATIONS[DEFAULT_LANGUAGE].get(key, key)

  return translation


def localize_answer(answer_texts, lang=DEFAULT_LANGUAGE):
  """
    If answer_texts is a dictionary with language keys,
    return the version matching the chosen language.
    Example:
        answer_texts = {"en": "Hello", "hi": "नमस्ते"}
    """
  if isinstance(answer_texts, dict):
    return answer_texts.get(lang) or answer_texts.get(DEFAULT_LANGUAGE) or ""
  return str(answer_texts)


def available_languages():
  """Return the list of supported language codes."""
  return list(TRANSLATIONS.keys())


def set_default_language(lang_code):
  """Change global default language."""
  global DEFAULT_LANGUAGE
  if lang_code in TRANSLATIONS:
    DEFAULT_LANGUAGE = lang_code


# ------------------------------------------------------
# Example usage (for testing)
# ------------------------------------------------------
if __name__ == "__main__":
  print("🌐 Supported languages:", available_languages())

  for lang in ["en", "hi", "ta"]:
    print("\n---", lang.upper(), "---")
    print(translate("app_title", lang))
    print(translate("tagline", lang))
    print(translate("get_started", lang))
    print(translate("disclaimer", lang))

