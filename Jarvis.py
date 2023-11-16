import speech_recognition as sr
import pyttsx3
import requests
import datetime
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice input
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print(f"User: {command}")
        except sr.UnknownValueError:
            print("Sorry, I didn't get that. Please repeat.")
            command = take_command()

    return command


# Function to execute commands
def execute_command(command):
    if "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        result = search_wikipedia(query)
        speak("According to Wikipedia, " + result)
    if "hello jarvis" in command:
        speak("Hello! I am Jarvis signing in")
    if "joke" in command:
        speak("Which is the largest gate? Colgate")
    elif "today date" in command:
        today_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {today_date}")
    elif "good bye" in command:
        speak("Jarvis Signing Out")
        return True  # Return True to indicate exit
    elif "what is the time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "facebook" in command:
        speak("Opening facebook.")
        webbrowser.open("https://www.facebook.com/")
    elif "physics wallah" in command:
        speak("Opening Physics Wallah.")
        webbrowser.open("https://www.pw.live/")
    elif "amazon" in command:
        speak("Opening Amazon.")
        webbrowser.open("https://www.amazon.in/")
    elif "flipkart" in command:
        speak("Opening flipkart.")
        webbrowser.open("https://www.flipkart.com/")
    elif "whatsapp" in command:
        speak("Opening Whatsapp.")
        webbrowser.open("https://web.whatsapp.com/")
    elif "i will talk you later" in command:
        speak("Goodbye! Have a great day!")
        return True
    elif "chat gpt" in command:
        speak("Opening Chat Gpt.")
        webbrowser.open("https://chat.openai.com/")
    elif "instagram" in command:
        speak("Opening instagram.")
        webbrowser.open("https://www.instagram.com/")
    elif ("thank") in command:
        speak("Jarvis Signing out!")
        return True
    elif "play sleepy songs" in command:
        speak("Ok a smooth tune is playing.")
        webbrowser.open("https://www.youtube.com/watch?v=EOui-WN9vK0")
    elif "play a song" in command:
        speak("Ok a song is playing.")
        webbrowser.open("https://www.youtube.com/watch?v=5oExKMYIE9U")
    elif "play sleepy song" in command:
        speak("Ok a smooth tune is playing.")
        webbrowser.open("https://www.youtube.com/watch?v=EOui-WN9vK0")
    elif "pinterest" in command:
        speak("Opening Pinterest.")
        webbrowser.open("https://in.pinterest.com/")
    elif "twitter" in command:
        speak("Opening Twitter.")
        webbrowser.open("https://twitter.com/?lang=en")
    elif "x" in command:
        speak("Opening X.")
        webbrowser.open("https://twitter.com/?lang=en")
    elif "create thumbnail" in command:
        speak("You can watch this for creating thumbnail.")
        webbrowser.open("https://www.youtube.com/watch?v=VqBeUXN_XHw")
    elif "today date" in command:
        speak("Showing the current Date.")
        webbrowser.open(
            "https://www.bing.com/search?q=current+date+in+india&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=current+date+in+india&sc=11-21&sk=&cvid=18D392FC195E40B6A14FACCB2948F1BB&ghsh=0&ghacc=0&ghpl=")
    elif "quora" in command:
        speak("Opening Quora.")
        webbrowser.open("https://www.quora.com/")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com/")
    # ... (your other commands)
    else:
        speak("I'm sorry, I don't understand that command.")

# Function to search Wikipedia using requests library
def search_wikipedia(query):
    user_agent = "MyJarvis/1.0 (https://github.com/yourusername/MyJarvis)"
    headers = {"User-Agent": user_agent}
    url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro&titles={query}"

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        page_id = next(iter(data["query"]["pages"]))
        extract = data["query"]["pages"][page_id]["extract"][:200]  # Displaying the first 200 characters of the extract
        return extract
    except Exception as e:
        print(f"Error searching Wikipedia: {e}")
        return "Sorry, I couldn't find information on that topic."

# Main program loop
while True:
    command = take_command()
    if execute_command(command):

        break  # Break out of the loop when execute_command returns True
