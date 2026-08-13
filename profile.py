import tkinter as tk
from tkinter import messagebox

from database import save_profile



def open_profile(parent):


    profile = tk.Toplevel(parent)

    profile.title(
        "User Profile"
    )

    profile.geometry(
        "400x450"
    )


    tk.Label(
        profile,
        text="USER PROFILE",
        font=("Arial",20,"bold")
    ).pack(pady=20)



    fields = {}

    for label in [
        "Name",
        "Age",
        "Gender",
        "Email",
        "Phone"
    ]:

        tk.Label(
            profile,
            text=label
        ).pack()


        entry=tk.Entry(
            profile,
            width=30
        )

        entry.pack(
            pady=5
        )

        fields[label]=entry



    def save():

        save_profile(
            fields["Name"].get(),
            fields["Age"].get(),
            fields["Gender"].get(),
            fields["Email"].get(),
            fields["Phone"].get()
        )


        messagebox.showinfo(
            "Success",
            "Profile Saved"
        )



    tk.Button(
        profile,
        text="Save Profile",
        bg="green",
        fg="white",
        width=20,
        command=save
    ).pack(
        pady=20
    )