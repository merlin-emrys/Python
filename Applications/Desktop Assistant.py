from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
    print(audio)
    tts= gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('sound audio.mp3')

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am ready for your next command")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said: "+command + "\n" )
    except sr.UnknownValueError:
        assistant(myCommand())
    return command

def assistant(command):
    if 'open Reddit python' in command:
        edge_path = 'C:/Windows/SystemApps/Microsoft.MicrosoftEdge_8wekyb3d8bbwe'
        url = 'https://www.reddit.com/python'
        webbrowser.get(edge_path).open(url)

    if 'what\'s up' in command:
        talkToMe('Chillin bro')

    if 'email' in command:
        talkToMe('Who is the recipient')
        recipient = myCommand()
        if 'Lady' in recipient:
            talkToMe('What should I say')
            content = myCommand()

            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()

            mail.starttls()
            mail.login('','')

            
            mail.sendmail('Person name','email address', content)
            mail.close()

            talkToMe('Email sent')

talkToMe('I am ready for your command')
while True:
    assistant(myCommand())






            
