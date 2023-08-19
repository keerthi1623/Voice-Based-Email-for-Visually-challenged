import pyttsx3
def text_to_speech(text, voice_id=None, rate=200):
    engine = pyttsx3.init()
    if voice_id:
        engine.setProperty('voice', voice_id)
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

if _name_ == "_main_":
    # Replace 'VOICE_ID' with the ID of the voice you want to use
    # If not specified, pyttsx3 will use the default voice.
    # For example, on Windows, you can use 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    voice_id = 'VOICE_ID'
    text = input("Enter the text to convert to speech: ")
    rate = 110
    text_to_speech(text, voice_id, rate)
