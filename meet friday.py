
import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import os
import pygetwindow as gw


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

recognizer = sr.Recognizer()

user_name = "Ameen"
assistant_name = "Friday"

def close_youtube_tab():
    for window in gw.getWindowsWithTitle('YouTube'):
        try:
            window.close()
            return True
        except Exception as e:
            print("Error closing YouTube tab:", e)
    return False

def cmd():
    with sr.Microphone() as source:
        print('Clearing background noise... Please wait.')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Listening...')
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language='en-US').lower()
            print('You said:', text)
        except sr.WaitTimeoutError:
            print("Listening timed out. Try again.")
            return True
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return True
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition.")
            return True

    if f"hi {assistant_name.lower()}" in text:
        response = f"Hi {user_name}, how can I help you?"
        print(response)
        engine.say(response)
        engine.runAndWait()

    elif 'bye assistant' in text or 'exit' in text or 'shutdown' in text:
        engine.say("Goodbye! Shutting down.")
        engine.runAndWait()
        return False

    elif 'open visual studio code' in text:
        engine.say('Opening Visual Studio Code.')
        engine.runAndWait()
        program_path = r"C:\Program Files\Microsoft VS Code\Code.exe"
        subprocess.Popen([program_path])

    elif 'open chrome' in text:
        engine.say('Opening Chrome...')
        engine.runAndWait()
        program_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program_path])

    elif 'close chrome' in text:
        engine.say('Closing Chrome...')
        engine.runAndWait()
        os.system("taskkill /f /im chrome.exe")

    elif 'open youtube' in text:
        engine.say('Opening YouTube...')
        engine.runAndWait()
        webbrowser.open('https://www.youtube.com')

    elif 'close youtube' in text:
        engine.say('Closing YouTube...')
        engine.runAndWait()
        closed = close_youtube_tab()
        if not closed:
            engine.say("Could not find a YouTube tab to close.")
            engine.runAndWait()

    elif 'time' in text:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print("Current time:", current_time)
        engine.say(f"The time is {current_time}")
        engine.runAndWait()

    elif 'play' in text:
        engine.say('Opening YouTube and playing your request...')
        engine.runAndWait()
        pywhatkit.playonyt(text)

    else:
        engine.say("Sorry, I didn't understand that.")
        engine.runAndWait()

    return True

print(f"{assistant_name} is now online. Say 'Hi {assistant_name}' to begin.")
engine.say(f"{assistant_name} is now online. Say 'Hi {assistant_name}' to begin.")
engine.runAndWait()

keep_listening = True
while keep_listening:
    keep_listening = cmd()

