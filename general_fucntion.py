from hourly_forecast import get_hourly_weather
import os

exit_to_main = False

def user_next_action(lat_location, lon_location, api_key):
    while True:
        user_choice = input(
            "\nWhat would you like to do next?\n"
            "Enter 'H' to see the hourly forecast,\n"
            "'F' to see the 5-day forecast,\n"
            "'Y' to search for another location,\n"
            "or 'N' to return to the main menu: "
        ).strip().upper()

        if user_choice == "H":
            os.system('clear')
            hourly_weather = get_hourly_weather(lat_location, lon_location, api_key)
            continue

        elif user_choice == "F":
            os.system('clear')
            print("5-day forecast pending....")
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

