from modules.weather_module import get_hourly_weather
from modules.settings_module import load_settings
import os

settings = load_settings()



def user_next_action(lat_location, lon_location, api_key):
    while True:
        user_choice = input(
            "\nWhat would you like to do next?\n"
                        "Enter\n"
            "'H' to see the hourly forecast,\n"
            "'F' to see the 5-day forecast,\n"
            "'Y' to search for another location,\n"
            "'N' to return to the main menu: "
        ).strip().upper()

        if user_choice == "H":
            os.system('clear')
            hourly_weather = get_hourly_weather(lat_location, lon_location, api_key, settings["units"])
            continue

        elif user_choice == "F":
            os.system('clear')
            print("5-day forecast under construction....")
            continue # Back to main menu

        elif user_choice == 'Y':
            os.system('clear')
            break # Restart the inner loop to search for another city

        elif user_choice == "N":
            os.system('clear')
            print("returning to main menu...")
            return "main_menu"

        else:
            os.system('clear')
            print("Invalid input. Please enter H, F, Y, or N.")

