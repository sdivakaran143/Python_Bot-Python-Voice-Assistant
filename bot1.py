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
    mus ="J:\\Audio Song\\01\\my music"
    fil = os.listdir(mus)
    m = random.choice(fil)
    os.startfile(os.path.join(mus,m))
    exit()

def work(inp):

    if "diva" in inp:
        speak("hai iam hear iam happy to help you Dear")

    elif 'music' in inp:
            speak("playing music ")
            speak("thank you have a nice day")
            music()
            exit()

            
    elif "wind up" in inp:
        speak("thank you have a nice day")
        exit()

    elif "gururaj"in inp:
        speak("guru raj is a hacker his father name is ravichandran he has a two besties and one sweet lover at college he is wellknown hacker in ksr college ")

    elif "profile image" in inp:
        loc="C:\\Users\\SAARAL\\Downloads\\unnamed.jpg"
        os.startfile(loc)
    
    elif "facebook" in inp:
        webbrowser.open('facebook.com')
        exit()

    elif "default" in inp:
        speak("could you say it again")

    elif "photoshop" in inp:
        speak("opening photoshop")
        speak("thank you have a nice day")
        loc="C:\\Program Files\\Adobe\\Adobe Photoshop CS6 (64 Bit)\\Photoshop.exe"
        os.startfile(loc)
        exit()
    
    else :
        speak("if you want to search in wikipedia say yes ")
        speak("if you want to search in google say ok ")
        option=hear().lower()
        if "yes"in option:
            speak(wikipedia.summary(inp, sentences=4))
        if "ok"in option:
            speak("opening webpage")
            webbrowser.open(inp)

           

if __name__ == "__main__":
    speak("hai i am  D iam a chatbot happy to assist you")

    while True: 
        speak("speak")   
        inp=hear().lower()
        work(inp)
        
            