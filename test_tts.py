import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 170)

while True:
    text = input("You: ")

    if text.lower() == "exit":
        engine.say("Goodbye")
        engine.runAndWait()
        break

    engine.say(text)
    engine.runAndWait()