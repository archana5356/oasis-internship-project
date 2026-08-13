"""
=========================================================
            AI Voice Assistant
        Command Processing Module
=========================================================
Author  : Archana T S
Version : 1.0
=========================================================
"""

import datetime
import webbrowser
import pyjokes


from tts import speak
from tts import speak


def process_command(command):
    """
    Process the user's voice command and return a response.
    """

    command = command.lower()

    # -----------------------------
    # Greeting
    # -----------------------------
    if "hello" in command or "hi" in command:
        response = "Hello! How can I help you today?"

    # -----------------------------
    # Time
    # -----------------------------
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {current_time}"

    # -----------------------------
    # Date
    # -----------------------------
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        response = f"Today's date is {current_date}"

    # -----------------------------
    # Google Search
    # -----------------------------
    elif command.startswith("search"):
        query = command.replace("search", "").strip()

        if query:
            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )
            response = f"Searching Google for {query}"
        else:
            response = "Please tell me what you want to search."

    # -----------------------------
    # Open YouTube
    # -----------------------------
    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        response = "Opening YouTube."

    # -----------------------------
    # Open Google
    # -----------------------------
    elif "google" in command:
        webbrowser.open("https://www.google.com")
        response = "Opening Google."

    # -----------------------------
    # Joke
    # -----------------------------
    elif "joke" in command:
        response = pyjokes.get_joke()

    # -----------------------------
    # Exit
    # -----------------------------
    elif "exit" in command or "bye" in command:
        response = "Goodbye! Have a wonderful day."

    # -----------------------------
    # Unknown Command
    # -----------------------------
    else:
        response = (
            "Sorry, I didn't understand that command."
        )

    speak(response)

    return response
def process_command(command):

    if "hello" in command:
        speak("Hello Archana!")

    elif "time" in command:
        speak("The current time is 10 AM")