"""
=========================================================
                    AI Voice Assistant
=========================================================
Author  : Archana T S
Version : 1.0.0
Description : Main entry point of the AI Voice Assistant
=========================================================
"""

import customtkinter as ctk
from tkinter import messagebox

# Import project modules
from speech import listen
from tts import speak
from command_processor import process_command


class VoiceAssistantApp:

    def __init__(self):

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()

        self.root.title("🤖 AI Voice Assistant")

        self.root.geometry("1000x650")

        self.root.resizable(False, False)

        self.create_widgets()

    # --------------------------------------------------

    def create_widgets(self):

        title = ctk.CTkLabel(
            self.root,
            text="🤖 AI Voice Assistant",
            font=("Segoe UI", 30, "bold")
        )

        title.pack(pady=20)

        self.status = ctk.CTkLabel(
            self.root,
            text="Status : Ready",
            font=("Segoe UI", 18)
        )

        self.status.pack()

        self.chat = ctk.CTkTextbox(
            self.root,
            width=900,
            height=380,
            font=("Consolas", 15)
        )

        self.chat.pack(pady=20)

        self.chat.insert("end", "Assistant : Hello! I am your AI Voice Assistant.\n\n")

        button_frame = ctk.CTkFrame(self.root)

        button_frame.pack(pady=10)

        self.listen_btn = ctk.CTkButton(
            button_frame,
            text="🎤 Speak",
            width=180,
            height=45,
            command=self.start_listening
        )

        self.listen_btn.grid(row=0, column=0, padx=15)

        self.clear_btn = ctk.CTkButton(
            button_frame,
            text="🗑 Clear",
            width=180,
            height=45,
            command=self.clear_chat
        )

        self.clear_btn.grid(row=0, column=1, padx=15)

        self.exit_btn = ctk.CTkButton(
            button_frame,
            text="❌ Exit",
            width=180,
            height=45,
            fg_color="red",
            hover_color="darkred",
            command=self.close
        )

        self.exit_btn.grid(row=0, column=2, padx=15)

    # --------------------------------------------------

    def start_listening(self):

        self.status.configure(text="🎤 Listening...")

        self.root.update()

        command = listen()

        if not command:
            self.status.configure(text="Ready")
            return

        self.chat.insert("end", f"You : {command}\n")

        if command.lower() in ["exit", "quit", "bye", "goodbye"]:

            speak("Goodbye!")

            self.close()

            return

        response = process_command(command)

        if response:

            self.chat.insert("end", f"Assistant : {response}\n\n")

            speak(response)

        self.chat.see("end")

        self.status.configure(text="Ready")

    # --------------------------------------------------

    def clear_chat(self):

        self.chat.delete("1.0", "end")

    # --------------------------------------------------

    def close(self):

        if messagebox.askyesno("Exit", "Close AI Voice Assistant?"):

            self.root.destroy()

    # --------------------------------------------------

    def run(self):

        speak("Hello Archana. Welcome back.")

        self.root.mainloop()


# ======================================================

if __name__ == "__main__":

    app = VoiceAssistantApp()

    app.run()