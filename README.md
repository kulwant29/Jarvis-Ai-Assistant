# Jarvis AI Voice Assistant
* Jarvis is a simple voice-controlled assistant built in Python. The project was created to explore how voice recognition, text-to-speech and modern AI APIs can be combined to build an interactive assistant.

* It can listen to voice commands, respond using speech, open system applications, play music and answer general questions using Google's Gemini AI.

## Features

* Voice command recognition
* AI responses using Google Gemini
* Text-to-speech responses
* Open system applications
* Play music from
* Fetch latest news
* Smart short AI responses

## Technologies Used

* Python
* SpeechRecognition
* PyAudio
* pyttsx3
* Google Gemini API
* News API
* Webbrowser

## Project Structure

Jarvis-AI-Assistant
│
├── main.py
├── geminiApi.py
├── musicLibrary.py
├── requirements.txt
├── .gitignore
└── README.md

## Installation

1. Clone the repository

git clone https://github.com/kulwant29/Jarvis-Ai-Assistant.git

2. Navigate to project folder

cd Jarvis-Ai-Assistant

3. Install dependencies

pip install -r requirements.txt

4. Create a '.env' file and add your API keys

Gemini_Api_Key=your_gemini_api_key
News_Api_Key=your_news_api_key

5. Run the assistant

python main.py

## Example Commands
* "Open Google"
* "Open Youtube"
* "Open File Explorer"
* "Open Spotify"
* "Play {song_name}"
* "What is Artificial Intelligence?"
* "Tell me the news"

## Future Improvements
* Add wake word detection
* Add GUI interface
* Add system automation commands
* Add local AI model support

## Author
Kulwant Saini

* This project was built as part of my learning process while experimenting with voice assistants in Python.