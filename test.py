"""
=========================================
        Speech Recognition Test
=========================================
"""

from speech import listen


def main():
    print("=" * 50)
    print("🎤 AI Voice Assistant - Microphone Test")
    print("=" * 50)
    print("Speak something...")
    print("Say 'exit' to quit.")
    print("=" * 50)

    while True:
        command = listen()

        if command:
            print(f"\n✅ You said: {command}")

            if command.lower() == "exit":
                print("👋 Exiting...")
                break
        else:
            print("⚠️ Please try speaking again.")


if __name__ == "__main__":
    main()