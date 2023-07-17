import speech_recognition as sr
import pyttsx3,os,random,time,webbrowser,wikipedia 

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
         

if __name__ == "__main__":
    speak("hai i am sara iam a chatbot happy to assist you")
    while True: 
        # speak("speak")   
        inp=hear().lower()
        work(inp)
        