import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
recognizer = sr.Recognizer()

newsapi = os.getenv("News_Api_Key")

# ---------------- TTS ---------------

def speak(text):
    engine = pyttsx3.init() 
    # rate = engine.getProperty("rate")
    # engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()


# --------------- Gemini Setup ---------------

api_key = os.getenv("Gemini_Api_Key")
client = genai.Client(api_key=api_key)

def AiProcess(command):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"You are Jarvis, a smart AI assistant. Reply smartly in one short sentence: {command}"
    )
    return response.text


# --------------- To open System Applications ---------------
def open_app(app_name):
    try:
        os.system(f"start {app_name}")
        speak(f"Opening {app_name},sir")
    except:
        speak("Application not found")


# --------------- Command Processor ---------------
def processCommand(c):
    if "open google" in c.lower():
        speak("Opening google,sir")
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        speak("Opening facebook,sir")
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        speak("Opening youtube,sir")
        webbrowser.open("https://www.youtube.com/")

    elif "open files" or "open file explorer" in c.lower():
        speak("Opening file explorer,sir")
        os.system("explorer")

    elif "open" in command:
        app = command.replace("open","").strip()
        open_app(app)

    
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "", 1).strip()
        link = musicLibrary.music[song]
        if link:
            speak(f"Playing {song} sir")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find that song")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract the articles
            articles = data.get("articles", [])

            # Prints the headlines
            for articles in articles:
                speak(articles('title'))

    else:
        # Let Gemini handle the request
        output = AiProcess(command)
        speak(output)


# --------------- Main --------------
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
            word = r.recognize_google(audio)
            print("recognizing...")
            if (word.lower() == "jarvis"):
                speak("Hello sir")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

