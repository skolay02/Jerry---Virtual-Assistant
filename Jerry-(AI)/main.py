import speech_recognition as sr
import webbrowser
import pyttsx3
import requests


recognizer = sr.Recognizer();
engine = pyttsx3.init()

# 0-Male voice,  1-Female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#Rate of speech
rate = engine.getProperty('rate')   
engine.setProperty('rate', 175) 

newsapi = "c2184e915f6d44e0943713fa4ae17dd4"

def speak(text):
    engine.say(text)
    engine.runAndWait()


#Music records
music = {
    "saudebaazi": "https://www.youtube.com/watch?v=CxAWKewvooo",
    "kk": "https://www.youtube.com/watch?v=leT7O4mMtsc",
    "khairiyat": "https://www.youtube.com/watch?v=hoNb6HuNmU0",
    "shayad": "https://www.youtube.com/watch?v=MJyKN-8UncM"
}

#Question tags
qtag = ["how", "what", "why", "when", "where", "who", "which", "whom", "whose"]



def processCommand(c):

    #Opening any website
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open amazon" in c.lower():
        webbrowser.open("https://www.amazon.in")
    elif "play games" in c.lower():
        webbrowser.open("https://www.y8.com")
    

    #Whatever question the google asks here it will redirect to the respective google pg
    elif any(word in c.lower() for word in qtag):
        pg = "https://www.google.com/search?q="+c
        webbrowser.open(pg)
        
         # Speak the query
        engine.say(f"Searching for {c}")
        engine.runAndWait()


    #Playing any song on Youtube
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music[song]
        webbrowser.open(link)


    
    #Reading news headlines
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
    



if __name__ == "__main__":
     speak("Initializing Jerry....")
     while True:
        # Listen for the wake word "Hexa"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source,duration=1)
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jerry"):
                speak("Hi there!")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jerry Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))