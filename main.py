import requests
from modules.geolocation_module import get_country_code, get_lon_lat_location, get_location_name
from modules.weather_module import get_location_weather, get_hourly_weather
from modules.saved_location import save_location_input, append_csv, print_csv, selection
from modules.general_function import user_next_action
from modules.settings_module import save_settings, load_settings, change_units_menu, save_settings_default, load_default, change_default
import os
import csv
from datetime import date
import sys
api_key = "9d155096c4339d42978deb57ae2027e2"
menu = ['Search Weather by Location', 'My Saved Locations', 'Historical Weather Lookup', 'Settings', 'Exit']
setting_menu = ['Change Tempreture Units', 'Change Default Location', 'Main Menu']
# Get today's date
today = date.today().strftime("%Y-%m-%d")


# Main Menu
while True:
    os.system('clear') # clear screen
    
    settings = load_settings()
    settings_default = load_default()

    city = settings_default.get("city")
    code = settings_default.get("country_code")
    lon1, lat1 = get_lon_lat_location(city, code, api_key)

    print(f"Location: {city} | Country Code: {code} ") 
    get_location_weather(lat1, lon1, api_key, settings["units"])

    next_action = input("Enter to go to the main menu, or Q to exit app \t").capitalize()
    if next_action == "Q":
        break

    elif next_action == "" :

        while True: 
            os.system('clear') # clear screen
            print("\n" + "=" * 37)
            print(" WEATHER APP ".center(37, "="))
            print("=" * 37 + "\n")

            for index, options in enumerate(menu, 1):
                print (f"{index}. {options}")

            print( "=" * 37 )
            menu_user_input = input(" Please enter your choice: ")


            if int(menu_user_input) == 1:
                while True:
                    os.system('clear') # clear screen
                    country_code = get_country_code()
                    location_name = get_location_name(country_code)
                    lat_location,lon_location = get_lon_lat_location(location_name, country_code, api_key)

                    os.system('clear') # clear screen
                    print(f"Location: {location_name} | Country Code: {country_code} ")        
                    get_location_weather(lat_location, lon_location, api_key, settings["units"])

                    save_location_answer = save_location_input()
                    data = [today, location_name, country_code]
                    if save_location_answer == "Y":
                        append_csv(data)
                    else:
                        os.system('clear')
                        print("✘ Location not saved.")
                    
                    action = user_next_action(lat_location,lon_location, api_key)

                    if action == "main_menu":
                        break

            if int(menu_user_input) == 2:
                os.system('clear')
                print_csv()
                location, code = selection()

                os.system('clear')
                lat,lon = get_lon_lat_location(location, code, api_key)
                print(f"Location: {location} | Country Code: {code} ")        
                get_location_weather(lat, lon, api_key, settings["units"])

                action = user_next_action(lat,lon, api_key)



            if int(menu_user_input) == 4:
                os.system('clear')
                print("\n" + "=" * 37)
                print(" Setting Menu ".center(37, "="))
                print("=" * 37 + "\n")

                for index, options in enumerate(setting_menu, 1):
                    print (f"{index}. {options}")

                print("=" * 37 )
                setting_user_input = input(" Please enter your choice: ")

                
                if int(setting_user_input) == 1:
                    os.system('clear')
                    change_default(settings_default)
                    continue

                if int(setting_user_input) == 2:
                    os.system('clear')
                    change_default(settings_default)
                    continue

                if int(setting_user_input) == 3:
                    break

            if int(menu_user_input) == 5:
                sys.exit()



            

       


            





            
                
            

            




                        
                

            



            








        # if "cloud" in description:
        #     print("It's cloudy today.")
        # else:
        #     print("🌞 No clouds today!")

