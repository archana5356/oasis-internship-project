import json
import os

# -----------------------------
# Folder & File Paths
# -----------------------------

DATA_FOLDER = "data"

HISTORY_FILE = os.path.join(DATA_FOLDER, "history.json")
FAVORITES_FILE = os.path.join(DATA_FOLDER, "favorites.json")


# -----------------------------
# Create Folder and Files
# -----------------------------

def create_files():

    os.makedirs(DATA_FOLDER, exist_ok=True)

    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as file:
            json.dump([], file)

    if not os.path.exists(FAVORITES_FILE):
        with open(FAVORITES_FILE, "w") as file:
            json.dump([], file)


create_files()


# -----------------------------
# History Functions
# -----------------------------

def save_history(city):

    city = city.strip().title()

    with open(HISTORY_FILE, "r") as file:
        history = json.load(file)

    if city not in history:
        history.append(city)

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def get_history():

    with open(HISTORY_FILE, "r") as file:
        return json.load(file)


def clear_history():

    with open(HISTORY_FILE, "w") as file:
        json.dump([], file, indent=4)


# -----------------------------
# Favorite Functions
# -----------------------------

def add_favorite(city):

    city = city.strip().title()

    with open(FAVORITES_FILE, "r") as file:
        favorites = json.load(file)

    if city not in favorites:
        favorites.append(city)

    with open(FAVORITES_FILE, "w") as file:
        json.dump(favorites, file, indent=4)


def get_favorites():

    with open(FAVORITES_FILE, "r") as file:
        return json.load(file)


def remove_favorite(city):

    city = city.strip().title()

    with open(FAVORITES_FILE, "r") as file:
        favorites = json.load(file)

    if city in favorites:
        favorites.remove(city)

    with open(FAVORITES_FILE, "w") as file:
        json.dump(favorites, file, indent=4)


def clear_favorites():

    with open(FAVORITES_FILE, "w") as file:
        json.dump([], file, indent=4)