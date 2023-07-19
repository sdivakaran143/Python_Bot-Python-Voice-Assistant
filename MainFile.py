import speech_recognition as sr
import pyttsx3,os,random,time,webbrowser,wikipedia 
from tkinter import *
engine = pyttsx3.init()
voices = engine.setProperty("rate",115)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def hear():                                                                 
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                             
        audio = r.listen(source)
    try:
        audio = r.recognize_google(audio, language='en-in')
        print("You said ",audio)
        return audio
    except:
        print("could not understand your audio")
        return "default"

def music():
    mus ="C:\\Users\\ASUS\\Music\\Playlists"
    fil = os.listdir(mus)
    m = random.choice(fil)
    os.startfile(os.path.join(mus,m))
    exit()

def work(inp):

    if "sara" in inp or "your name"in inp:
        speak("Hey iam Sara iam happy to help you Dear")

    elif 'music' in inp:
            speak("playing music ")
            speak("thank you have a nice day")
            music()
            exit()

    elif "wind up" in inp or "exit" in inp:
        speak("thank you have a nice day")
        exit()

    elif "facebook" in inp:
        webbrowser.open('facebook.com')
        speak("Iam happy to help you thankyou.. enjoy your moment with facebook ")
        exit()

    elif "default" in inp:
        pass
        # speak("could you say it again")

    elif ("search in google" in inp)or("search" in inp):
        speak("opening webpage")
        webbrowser.open(inp)
    
    else :
        try:
            speak(wikipedia.summary(inp, sentences=4))
        except:
            webbrowser.open(inp)
         

def handle_button_start(event):
    print("hello")
    speak("hai i am sara iam a chatbot happy to assist you")
    speak("speak")   
    inp=hear().lower()
    work(inp)

def handle_button_press(event):
    window.destroy()


window=Tk()
window.title("Voice Assistant")
window.minsize(100,50)
window.maxsize(200,100)
window.geometry("300x150+550+250")
text1=Label(window,text="Click start")
text1.pack()
button1=Button(window, text="Start")
button1.bind("<Button-1>",handle_button_start)
button1.pack()
button2 =Button(window, text=" Exit ",command=window.quit)
button2.pack()
window.mainloop()
