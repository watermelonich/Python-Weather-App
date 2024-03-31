import os
import requests

from flask import Flask, render_template

app = Flask(
    __name__,
    static_url_path="",
    static_folder="web/static",
    template_folder="web/templates",
)
API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"
CITY_NAME = "wellington"


@app.route("/")
def hello_world():
    return render_template("index.html", message="Hello, World!")


@app.route("/current")
def current():
    try:
        r = requests.get(
            f"{BASE_URL}/weather?q={CITY_NAME}&units=metric&appid={API_KEY}"
        )
        r.raise_for_status()
        data = r.json()

        current_weather = {
            "description": data["weather"][0]["description"].title(),
            "icon": data["weather"][0]["icon"],
            "name": data["name"],
            "temperature": data["main"]["temp"],
            "wind": data["wind"]["speed"],
        }

        return render_template("index.html", weather=current_weather)
    except requests.exceptions.ConnectionError as err:
        return f"Error: {err}"


@app.route("/forecast")
def forecast():
    r = requests.get(
        f"{BASE_URL}/onecall?lat={41.2924}&lon={174.7787}&units=metric&appid={API_KEY}"
    ).json()

    return render_template("index.html", forecast=r["daily"])


@app.errorhandler(404)
def page_not_found(error):
    return render_template("index.html", message=error), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
