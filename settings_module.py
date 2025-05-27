import csv
import json



def load_settings():
    try:
        with open("settings.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"units": "metric"}  # if nothing in file, return these as defaultdefault

def save_settings(settings):
    with open("settings.json", "w") as file:
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







