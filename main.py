"""
WeatherSphere - Professional Weather Dashboard

Main Application File

Author: Archana T S

Features:
- Real-time weather information
- OpenWeatherMap API integration
- Tkinter GUI dashboard
- Weather icons
- Temperature conversion
- Search history
"""


import tkinter as tk
from tkinter import messagebox

from gui import WeatherGUI



def start_application():

    try:

        # Create main window

        root = tk.Tk()


        # Application icon/title

        root.title(
            "WeatherSphere 🌤"
        )


        # Start GUI

        app = WeatherGUI(root)


        # Run application

        root.mainloop()



    except Exception as e:


        messagebox.showerror(
            "Application Error",
            f"Something went wrong:\n{e}"
        )



if __name__ == "__main__":

    start_application()