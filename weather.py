import requests
from geolocation_module import get_country_code, get_l👉on_lat_location, get_location_name
from city_weather_module import get_location_weather
from hourly_forecast import get_hourly_weather
import os
import csv
api_key = "9d155096c4339d42978deb57ae2027e2"
menu = ['Search Weather by Location', 'My Saved Locations', 'Historical Weather Lookup' 'Settings']


# Main Menu

exit_to_main = False
while True: 
    print("\n" + "=" * 37)
    print(" WEATHER APP ".center(37, "="))
    print("=" * 37 + "\n")

    for index, options in enumerate(menu, 1):
        print (f"{index}. {options}")

    print("\n" + "=" * 37 + "\n")

    print("\n" + "-" * 37)
    menu_user_input = input(" Please enter your choice: ")
    print("-" * 37 + "\n")



    if int(menu_user_input) == 1:
        while True:
            os.system('clear') # clear screen
            country_code = get_country_code()
            location_name = get_location_name(country_code)
            lat_location,lon_location = get_lon_lat_location(location_name, country_code, api_key)

            os.system('clear') # clear screen
            print(f"Location: {location_name} | Country Code: {country_code} ")        
            get_location_weather(lat_location, lon_location, api_key)
            while True:
                user_choice = input(
                    "What would you like to do next?\n"
                    "Enter 'H' to see the hourly forecast,\n"
                    "'F' to see the 5-day forecast,\n"
                    "'Y' to search for another city,\n"
                    "or 'N' to return to the main menu: "
                ).strip().upper()

                if user_choice == "H":
                    os.system('clear')
                    hourly_weather = get_hourly_weather(lat_location, lon_location, api_key)
                    continue

                elif user_choice == "F":
                    os.system('clear')
                    print("7-day forecast")
                    continue # Back to main menu

                elif user_choice == 'Y':
                    os.system('clear')
                    break # Restart the inner loop to search for another city

                elif user_choice == "N":
                    os.system('clear')
                    exit_to_main = True
                    break # Exit inner loop and return to main menu

                else:
                    os.system('clear')
                    print("Invalid input. Please enter H, F, Y, or N.")

            if exit_to_main:
                break  # break the city searching loop




                
        

     



    








# if "cloud" in description:
#     print("It's cloudy today.")
# else:
#     print("🌞 No clouds today!")

