import customtkinter as ctk

ctk.set_appearance_mode("Dark")

app = ctk.CTk()
app.geometry("400x300")
app.title("Test")

label = ctk.CTkLabel(app, text="CustomTkinter is Working!")
label.pack(pady=50)

app.mainloop()