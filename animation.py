"""
=========================================================
                AI Voice Assistant
=========================================================
Author  : Archana T S
Version : 1.0
=========================================================
"""

from speech import listen
from tts import speak
from command_processor import process_command

from animation import (
    loading_animation,
    welcome_banner,
    listening_animation,
    thinking_animation,
    speaking_animation
)


def main():

    # Startup animation
    loading_animation()

    # Banner
    welcome_banner()

    # Welcome speech
    speaking_animation()
    speak("Hello! I am your AI Voice Assistant.")
    speak("How can I help you today?")

    while True:

        # Listening animation
        listening_animation()

        command = listen()

        if not command:
            continue

        print(f"\nYou : {command}")

        # Thinking animation
        thinking_animation()

        if command.lower() in ["exit", "quit", "bye"]:

            speaking_animation()
            speak("Goodbye! Have a nice day.")
            break

        process_command(command)


if __name__ == "__main__":
    main()