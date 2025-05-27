import json
from modules.geolocation_module import get_country_code, get_location_name
from datetime import datetime

def load_settings():
    try:
        with open("settings_units.json", "r") as file:
            return json.load(file)  # returns dict like {"city":..., "country_code":..., ...}
    except FileNotFoundError:
        return {"units": "metric"}  # if nothing in file, return these as defaultdefault

def save_settings(settings):
    with open("settings_units.json", "w") as file:
        json.dump(settings, file)

def change_units_menu(settings):
    print("\nTemperature units Settings")
    print("1. Celsius (°C)")
    print("2. Fahrenheit (°F)")
    choice = input("Choose default temperature units (1 or 2): ")

    if choice == "1":
        settings["units"] = "metric"
        print("✔ Default units set to Celsius.")
    elif choice == "2":
        settings["units"] = "imperial"
        print("✔ Default units set to Fahrenheit.")
    else:
        print("Invalid choice. No changes made.")

    save_settings(settings)



def load_default():
    try:
        with open("settings_default.json", "r") as file:  # Try to open 'settings.json' in read mode
            return json.load(file)        
    except FileNotFoundError:
        # If the file doesn't exist, print a message and return None for both values
        print("No default location saved")
        return {}
    

def save_settings_default(settings):
    with open("settings_default.json", "w") as file:
        json.dump(settings, file)


def change_default(settings):
    choice = input("Would you like to change the default location? Y/N ").capitalize()

    if choice == "Y":
        code = get_country_code()
        location = get_location_name(code)

        settings["city"] = location
        settings["country_code"] = code
        settings["saved_on"] = datetime.now().strftime("%Y-%m-%d")

        save_settings_default(settings)
        print(f"Default location updated to: {location}, {code}")

    else:
        print("No changes made to default location.")

    














