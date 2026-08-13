"""
=========================================================
                Text To Speech Module
=========================================================
Author  : Archana T S
Version : 1.0
=========================================================
"""

import pyttsx3

# Initialize engine
engine = pyttsx3.init()

# Voice settings
voices = engine.getProperty("voices")

# Female voice (change to voices[0] if preferred)
if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)
else:
    engine.setProperty("voice", voices[0].id)

# Speed
engine.setProperty("rate", 170)

# Volume (0.0 to 1.0)
engine.setProperty("volume", 1.0)


def speak(text):
    """
    Convert text to speech.
    """

    print(f"🤖 Assistant: {text}")

    engine.say(text)
    engine.runAndWait()


def stop():
    """
    Stop speaking.
    """

    engine.stop()


if __name__ == "__main__":

    speak("Hello Archana. Welcome to AI Voice Assistant.")
    speak("This is a text to speech test.")     