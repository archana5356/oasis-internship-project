import requests


def get_location():

    try:

        response = requests.get(
            "https://ipinfo.io/json"
        )

        data=response.json()

        return data.get(
            "city",
            "London"
        )


    except:

        return "London"