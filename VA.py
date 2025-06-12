#A Module is a Python file consisting of
#variables,functions,classes
'''import day1
print(dir(day1))
#dir -->gives list of all available methods
day1.sample()
'''
#Give some text and convert that to audio
#gTTS -->Google Text to Speech
import gtts
#print(dir(gtts)) #gives list of available methods
from gtts import gTTS
#data = gTTS("Hope you guys are following")
#we will save in a audio file
#data.save("hey.mp3")

#to change language and accent
'''data = gTTS("hey guys hope you had good lunch",
            lang = 'fr')
data.save('new.mp3')

import playsound
data = gTTS("We are in Lab6 in MIC College")
data.save("hello.mp3")
playsound.playsound("hello.mp3")

Make our Virtual  Assistant to perform below actions
1)Conversation 2)Datetime 3)Opening browser
4)Locating maps 5)Email automation
'''
import speech_recognition as sr #aliasing
import playsound
from gtts import gTTS
import uuid
import os

#Define Function to understand what we are speaking
def listen():
    """Listening function to respond what we speak"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Start talking now...") #own statement
        audio = r.listen(source,phrase_time_limit=5) #time limit is user interest
    data=""
    try:
        data = r.recognize_google(audio,language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you speak louder")
    except sr.RequestError as e:
        print("Microphone is not working")
    return data
    #tts = gTTS(text=data)
    #tts.save("speech.mp3")
    #playsound.playsound("speech.mp3")
#listen()
        
#Create a Function to respond back
def respond(String):
    """Function for responding back"""
    tts = gTTS(text=String)
    tts.save("Speech.mp3")
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

#Create your Virtual Assitant with defined actions
def virtual_asstnt(data):
    """Give your desired actions"""
    if "how are you" in data:
        listening = True
        respond("I am good hope you are doing well")
respond("Hey Akhil how are you?") #frst greeting
listening=True
while listening==True:
    data = listen()
    listening = virtual_asstnt(data)












