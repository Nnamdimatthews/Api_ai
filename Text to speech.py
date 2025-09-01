import speech_recognition as sr
import pyttsx3
from googletrans import Translator

def speak_text(text, lang='en'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')

    if lang == 'en':
        engine.setProperty('voice', voices[1].id)
    elif lang == 'es':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[0].id)

    engine.say(text)
    engine.runAndWait()
    def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('🗣️ Please speak now in English...')
        audio = recognizer.listen(source)

    try:
        print('🕵️ Recognizing speech...')
        text = recognizer.recognize_google(audio, language="en-US")
        print(f'✅ You said: {text}')
        return text
    except sr.UnknownValueError:
        print('❌ Could not understand the audio.')
    except sr.RequestError as e:
        print(f'❌ API Error: {e}')
        return ""
    def translate_text(text, target_laguage="es"):
        translator = Translator
translation = Translator.translate(text, dest = target_language)
print(f"???? Translated text: {translation.text}")
return translation.text

def display_language_options():
    print("???? Available translation languages:")
    print("1. Hindi ('hi')")
    print("2. Tamil ('ta')")
    print("3. Telugu ('te')")
    print("4. Bengali ('bn')")
    print("5. Marathi ('r')")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")
choice = input("Please select the target language number (1-8): ")
language_dict = {
    "1": "hi",
    "2": "ta",
    "3": "te",
    "4": "kn",
    "5": "mr",
    "6": "gu",
    "7": "ml",
    "8": "pa"
    }
    return langauge_dict.get(choice, "es")
def main():
    target_language = display_language_options()
    original_text = speech_to_text()

    if original_text:
        translated_text = translate(original_text, target_language = target_language)
        speak_text(transleted_text, language="en")
        print("✅ Translation spoken out!")
if __name__ == " __main__":
    main()