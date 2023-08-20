import speech_recognition as sr
import pandas as pd
import pyttsx3

def text_to_speech(text, voice_id=None, rate=200):
    engine = pyttsx3.init()
    if voice_id:
        engine.setProperty('voice', voice_id)
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def process_email_specification(text):
    if "email" in text:
        text_to_speech("Please provide the email address.")
        email_choice = recognize_speech()
        if email_choice in df['email'].values:
            selected_row = df[df['email'] == email_choice].iloc[0]
            text_to_speech(f"Title: {selected_row['title']}")
            text_to_speech(f"Message: {selected_row['message']}")
        else:
            text_to_speech("Email address not found.")
    elif "time" in text:
        text_to_speech("Please specify the number of top recent emails you want to read.")
        num_emails = int(recognize_speech())
        top_rows = df.nlargest(num_emails, 'time')
        for index, row in top_rows.iterrows():
            text_to_speech(f"Email Address: {row['email']}")
            text_to_speech(f"Title: {row['title']}")
            text_to_speech(f"Message: {row['message']}")
    else:
        text_to_speech("Invalid choice.")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Please say your choice...")
        audio = recognizer.listen(source)
        try:
            choice = recognizer.recognize_google(audio).lower()
            print("User choice:", choice)
            return choice
        except sr.UnknownValueError:
            print("Sorry, could not understand your speech.")
            return None

def main():
    text_to_speech("Welcome! This is your email reader.")
    text_to_speech("Say 'email' to read by email address or 'time' to read by timestamps.")
    user_choice = recognize_speech()
    process_email_specification(user_choice)

if __name__ == "__main__":
    main()
