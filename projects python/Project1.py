#MY FIRST PROJECT
# ROBO SPEAKER

#For Mac
# import os

# if __name__ == '__main__':
#     print("Welcome to RoboSpeaker 11.1 Created by Harsh")
#     while True:
#         x = input("Enter what you want me to speak: ")
#         command = f"say {x}" 
#         os.system(command)


#For Windows
import pyttsx3
if __name__ == '__main__':
    text_to_speech = pyttsx3.init()
    while True:
        word = input("Enter your command: ")
        if word == 'q':
            break
        text_to_speech.say(word)
        text_to_speech.runAndWait()



