import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
from datetime import datetime

from weather_api import get_weather

from storage import (
    save_history,
    get_history,
    add_favorite,
    get_favorites
)


class WeatherGUI:


    def __init__(self, root):

        self.root = root

        self.root.title(
            "🌤 WeatherSphere - Professional Weather Dashboard"
        )

        self.root.geometry(
            "950x800"
        )

        self.root.resizable(
            False,
            False
        )

        self.root.configure(
            bg="#121212"
        )


        self.celsius = True
        self.current_temp = 0
        self.current_city = ""

        self.loading = False
        self.dot_count = 0


        self.create_widgets()

        self.update_clock()



    # ==================================
    # CREATE UI
    # ==================================

    def create_widgets(self):


        # Title

        title = tk.Label(
            self.root,
            text="🌤 WeatherSphere",
            font=("Arial",32,"bold"),
            bg="#121212",
            fg="white"
        )

        title.pack(
            pady=15
        )



        # Clock

        self.clock = tk.Label(
            self.root,
            font=("Arial",12),
            bg="#121212",
            fg="cyan"
        )

        self.clock.pack()



        # Search Area

        search_frame = tk.Frame(
            self.root,
            bg="#121212"
        )

        search_frame.pack(
            pady=15
        )



        self.city_entry = tk.Entry(
            search_frame,
            width=25,
            font=("Arial",16)
        )

        self.city_entry.grid(
            row=0,
            column=0,
            padx=5
        )


        # Enter key search

        self.city_entry.bind(
            "<Return>",
            lambda e:self.search_weather()
        )



        search_btn = tk.Button(
            search_frame,
            text="🔍 Search",
            font=("Arial",12,"bold"),
            bg="#2196F3",
            fg="white",
            width=12,
            command=self.search_weather
        )

        search_btn.grid(
            row=0,
            column=1,
            padx=5
        )



        refresh_btn = tk.Button(
            search_frame,
            text="🔄 Refresh",
            font=("Arial",12),
            width=10,
            command=self.search_weather
        )

        refresh_btn.grid(
            row=0,
            column=2,
            padx=5
        )



        toggle_btn = tk.Button(
            search_frame,
            text="°C / °F",
            width=10,
            command=self.toggle_temperature
        )

        toggle_btn.grid(
            row=0,
            column=3,
            padx=5
        )



        fav_btn = tk.Button(
            search_frame,
            text="⭐ Favorite",
            bg="#FFD700",
            width=12,
            command=self.add_to_favorites
        )

        fav_btn.grid(
            row=0,
            column=4,
            padx=5
        )



        # Weather Icon

        self.icon_label = tk.Label(
            self.root,
            bg="#121212"
        )

        self.icon_label.pack(
            pady=5
        )



        # Weather Card

        self.info_frame = tk.Frame(
            self.root,
            bg="#1E1E1E",
            width=820,
            height=280,
            relief="ridge",
            bd=2
        )

        self.info_frame.pack(
            pady=15
        )


        self.info_frame.pack_propagate(
            False
        )



        self.info_label = tk.Text(
            self.info_frame,
            font=("Arial",14),
            bg="#1E1E1E",
            fg="white",
            bd=0,
            wrap="word"
        )

        self.info_label.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )


        self.info_label.insert(
            tk.END,
            "Search a city to view weather information."
        )


        self.info_label.config(
            state="disabled"
        )



        # Status

        self.status = tk.Label(
            self.root,
            text="Ready",
            font=("Arial",12),
            bg="#121212",
            fg="lightgreen"
        )

        self.status.pack(
            pady=5
        )



        # Bottom Frame

        bottom = tk.Frame(
            self.root,
            bg="#121212"
        )

        bottom.pack(
            pady=15
        )



        # History

        history_frame = tk.Frame(
            bottom,
            bg="#121212"
        )

        history_frame.pack(
            side="left",
            padx=50
        )


        tk.Label(
            history_frame,
            text="📜 History",
            font=("Arial",16,"bold"),
            fg="white",
            bg="#121212"
        ).pack()



        self.history_box = tk.Listbox(
            history_frame,
            width=30,
            height=8
        )

        self.history_box.pack(
            pady=5
        )



        tk.Button(
            history_frame,
            text="🗑 Delete History",
            bg="red",
            fg="white",
            command=self.delete_history
        ).pack()



        # Favorites

        favorite_frame = tk.Frame(
            bottom,
            bg="#121212"
        )

        favorite_frame.pack(
            side="right",
            padx=50
        )


        tk.Label(
            favorite_frame,
            text="⭐ Favorites",
            font=("Arial",16,"bold"),
            fg="white",
            bg="#121212"
        ).pack()



        self.favorite_box = tk.Listbox(
            favorite_frame,
            width=30,
            height=8
        )

        self.favorite_box.pack(
            pady=5
        )


        tk.Button(
            favorite_frame,
            text="🗑 Delete Favorite",
            bg="red",
            fg="white",
            command=self.delete_favorite
        ).pack()



        self.load_saved_data()
            # ==================================
    # LIVE CLOCK ANIMATION
    # ==================================

    def update_clock(self):

        now = datetime.now().strftime(
            "%d-%m-%Y   %H:%M:%S"
        )

        self.clock.config(
            text=now
        )

        self.root.after(
            1000,
            self.update_clock
        )



    # ==================================
    # LOADING DOT ANIMATION
    # ==================================

    def loading_animation(self):

        if self.loading:

            dots = "." * (
                self.dot_count % 4
            )

            self.status.config(
                text="Fetching weather" + dots
            )


            self.dot_count += 1


            self.root.after(
                500,
                self.loading_animation
            )



    # ==================================
    # SEARCH WEATHER
    # ==================================

    def search_weather(self):

        city = self.city_entry.get()


        if city == "":

            messagebox.showwarning(
                "Warning",
                "Enter city name"
            )

            return



        self.loading = True
        self.dot_count = 0

        self.loading_animation()



        try:

            data = get_weather(city)



            self.loading = False



            self.current_city = city

            self.current_temp = float(
                data["temperature"]
            )



            weather_text = f"""

🌍 City :
{data['city']}


🌡 Temperature :
{data['temperature']} °C


🤔 Feels Like :
{data['feels']} °C


☁ Condition :
{data['condition']}


💧 Humidity :
{data['humidity']} %


🌬 Wind Speed :
{data['wind']} m/s


🔽 Pressure :
{data['pressure']} hPa


👁 Visibility :
{data['visibility']} km

"""


            self.info_label.config(
                state="normal"
            )


            self.info_label.delete(
                "1.0",
                tk.END
            )


            self.info_label.insert(
                tk.END,
                weather_text
            )


            self.info_label.config(
                state="disabled"
            )



            # Save History

            save_history(
                city
            )


            self.update_history()



            # Load icon

            self.load_weather_icon(
                data["icon"]
            )



            # Weather message

            condition = data["condition"].lower()



            if "rain" in condition:

                msg = "🌧 Rainy Weather"


            elif "cloud" in condition:

                msg = "☁ Cloudy Weather"


            elif "clear" in condition:

                msg = "☀ Clear Sunny Day"


            else:

                msg = "🌤 Weather Updated"



            self.status.config(
                text=msg
            )



            # Card animation

            self.animate_card()



        except Exception as e:


            self.loading = False


            messagebox.showerror(
                "Error",
                str(e)
            )



    # ==================================
    # WEATHER ICON
    # ==================================

    def load_weather_icon(self, icon):

        try:

            url = (
                "https://openweathermap.org/img/wn/"
                + icon
                + "@2x.png"
            )


            response = requests.get(
                url
            )


            image = Image.open(
                BytesIO(
                    response.content
                )
            )


            image = image.resize(
                (100,100)
            )


            photo = ImageTk.PhotoImage(
                image
            )


            self.icon_label.config(
                image=photo
            )


            self.icon_label.image = photo



        except:

            pass



    # ==================================
    # WEATHER CARD ANIMATION
    # ==================================

    def animate_card(self):

        colors = [
            "#1E1E1E",
            "#252525",
            "#303030",
            "#1E1E1E"
        ]


        def change(i):

            if i < len(colors):

                self.info_frame.config(
                    bg=colors[i]
                )


                self.root.after(
                    150,
                    lambda:
                    change(i+1)
                )


        change(0)



    # ==================================
    # TEMPERATURE CHANGE
    # ==================================

    def toggle_temperature(self):

        if self.current_temp == 0:

            return



        if self.celsius:


            fahrenheit = (
                self.current_temp * 9/5
            ) + 32


            self.status.config(
                text=f"{fahrenheit:.1f} °F"
            )


            self.celsius = False



        else:


            self.status.config(
                text=f"{self.current_temp:.1f} °C"
            )


            self.celsius = True
                # ==================================
    # ADD TO FAVORITES
    # ==================================

    def add_to_favorites(self):

        if self.current_city == "":

            messagebox.showwarning(
                "Warning",
                "Search a city first"
            )

            return



        add_favorite(
            self.current_city
        )


        self.update_favorites()


        messagebox.showinfo(
            "Favorite Added",
            f"{self.current_city} added to favorites"
        )



    # ==================================
    # UPDATE HISTORY LIST
    # ==================================

    def update_history(self):

        self.history_box.delete(
            0,
            tk.END
        )


        history = get_history()


        for city in history:

            self.history_box.insert(
                tk.END,
                city
            )



    # ==================================
    # UPDATE FAVORITES LIST
    # ==================================

    def update_favorites(self):

        self.favorite_box.delete(
            0,
            tk.END
        )


        favorites = get_favorites()


        for city in favorites:

            self.favorite_box.insert(
                tk.END,
                city
            )



    # ==================================
    # DELETE HISTORY
    # ==================================

    def delete_history(self):

        selected = self.history_box.curselection()


        if not selected:

            messagebox.showwarning(
                "Warning",
                "Select history item"
            )

            return



        self.history_box.delete(
            selected
        )



        messagebox.showinfo(
            "Deleted",
            "History removed"
        )



    # ==================================
    # DELETE FAVORITE
    # ==================================

    def delete_favorite(self):

        selected = self.favorite_box.curselection()


        if not selected:

            messagebox.showwarning(
                "Warning",
                "Select favorite city"
            )

            return



        self.favorite_box.delete(
            selected
        )


        messagebox.showinfo(
            "Deleted",
            "Favorite removed"
        )



    # ==================================
    # LOAD SAVED DATA
    # ==================================

    def load_saved_data(self):

        self.update_history()

        self.update_favorites()