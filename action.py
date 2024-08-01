import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action(data):
    user_data = data.lower()

    if "what is your name " in user_data:
        text_to_speech.text_to_speech("My name is Edith")
        return "My name is Edith"

    elif "hello" in user_data or "hi" in user_data :
        text_to_speech.text_to_speech("Hey, how can i help you?")
        return "Hey, how can i help you?"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("goodmorning Mam")
        return "goodmorning Mam"

    elif "whats the time" in user_data:
        current_time= datetime.datetime.now()
        Time = (str)(current_time)+ "Hour:", (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("Okay logging off")
        return "Okay logging off"

    elif " play music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        text_to_speech.text_to_speech("opening spotify now")
        return "opening spotify now"

    elif " open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("opening google now")
        return "opening google now"
    elif " Open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("opening youtube now")
        return "opening youtube now" 

    elif " whats the weather?" in user_data:
        ans= weather.weather()
        text_to_speech.text_to_speech(ans)
        return weather

    else:
        text_to_speech.text_to_speech("I can't understand")