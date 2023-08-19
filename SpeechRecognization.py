import speech_recognition as sr
import tts # import the tts.py file
def recognize_speech():
    # Create a speech recognition object
    recognizer = sr.Recognizer()
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
    try:
        # Use the recognizer to convert speech to text
        text = recognizer.recognize_google(audio)  # Use 'recognize_sphinx' for offline speech recognition
        print("You said:", text)
        tts.text_to_speech(text,'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0', 110)
    except sr.UnknownValueError:
        print("Sorry, could not understand your speech.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
if __name__ == "__main__":
    recognize_speech()
