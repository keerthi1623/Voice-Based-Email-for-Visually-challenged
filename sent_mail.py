text_to_speech("please,speak out email address")
new_email = recognize_speech()
if new_email:
    new_time = datetime.now()
    text_to_speech("now please speak out the subject")
    new_title = recognize_speech()
    if new_title:
        text_to_speech("Now it's time to sepak out the message")
        new_message = recognize_speech()
        text_to_speech("Done Successfully")
new_row = {
    'email': new_email,
    'time': new_time,
    'title': new_title,
    'message': new_message
}

df = df.append(new_row, ignore_index=True)
