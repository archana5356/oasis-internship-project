"""
=========================================================
                Speech Recognition Module
=========================================================
Author  : Archana T S
Purpose : Capture voice input from the microphone
=========================================================
"""

import speech_recognition as sr


def listen():
    """
    Listens to the user's voice and converts it to text.
    Returns:
        str: Recognized text (lowercase)
        
        None: If speech is not recognized
    """

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            print("\n🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        print("🔍 Recognizing...")

        command = recognizer.recognize_google(audio)

        print(f"👤 You: {command}")

        return command.lower()

    except sr.WaitTimeoutError:
        print("⌛ No speech detected.")
        return None

    except sr.UnknownValueError:
        print("❌ Sorry, I couldn't understand you.")
        return None

    except sr.RequestError:
        print("🌐 Internet connection is unavailable.")
        return None

    except OSError:
        print("🎤 Microphone not found.")
        return None

    except Exception as error:
        print(f"Error: {error}")
        return None


# ---------------------------------------------------------

if __name__ == "__main__":

    while True:

        text = listen()

        if text:
            print("Recognized:", text)

        if text == "exit":
            break