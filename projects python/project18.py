# import pyttsx3
# import speech_recognition as sr
# import webbrowser
# import datetime
# import pyjokes

# def sptext():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio =recognizer.listen(source)
#         try:
#             print("Recognizing...")
#             data = recognizer.recognize_google(audio)
#             print(data)
#             return data
#         except sr.UnknownValueError:
#             print("Please speak something")

# def speech(x):
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice',voices[0].id)
#     rate = engine.getProperty('rate')
#     engine.setProperty('rate',150)
#     engine.say(x)
#     engine.runAndWait()
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data.lower()
        except sr.UnknownValueError:
            print("Please speak something")

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Set voice type (0 for male, 1 for female)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)  # Set speech rate (words per minute)
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    while True:
        print("Listening for commands...")
        command = recognize_speech()

        if command:
            if "your name" in command:
                name = "My name is Jarvis."
                speak(name)
            elif "your boss" in command:
                boss = "My boss is Harsh."
                speak(boss)
            elif 'time' in command:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The current time is {current_time}")
            elif 'youtube' in command:
                webbrowser.open("https://www.youtube.com/")
            elif 'joke' in command:
                joke = pyjokes.get_joke()
                speak(joke)
            elif 'exit' in command or 'bye' in command:
                speak("Goodbye!")
                break
        else:
            print("Could not understand your command. Please try again.")
