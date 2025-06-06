import requests
from modules.weather_module import get_location_weather, get_hourly_weather, specific_date, date_input, get_country_code, get_lon_lat_location, get_location_name
from modules.saved_location import save_location_input, append_csv, print_csv, selection
from modules.general_function import user_next_action, main_menu_list, get_and_show_weather
from modules.settings_module import save_settings, load_settings, change_units_menu, save_settings_default, load_default, change_default
import os
import csv
from datetime import date
import sys
api_key = "9d155096c4339d42978deb57ae2027e2"
vc_api_key = "DEBDW5XCAE77P6L8XBTEBKX2C"
setting_menu = ['Change Tempreture Units', 'Change Default Location', 'Main Menu']
# Get today's date
today = date.today().strftime("%Y-%m-%d")


# Default Location Weather
while True:
    os.system('clear') # clear screen
    settings, settings_default = get_and_show_weather() # load setting for default location, and p

    while True:
        next_action = input("Enter to go to the main menu, or Q to exit app \t").capitalize()
        if next_action == "Q":
            sys.exit()
        elif next_action == "" :
            break
        else:
            print ("Invalid option selected: Enter to go to the main menu, or Q to exit app \t ")

    # Main Menu
    while True: 
        main_menu_list()
        menu_user_input = input(" Please enter your choice: ")

    # 1st Sub-Menu =  location weather - weather module
        if int(menu_user_input) == 1:
            while True:
                os.system('clear') # clear screen
                country_code = get_country_code()  # get country code
                location_name = get_location_name(country_code) # get location name
                lat,lon = get_lon_lat_location(location_name, country_code, api_key) # with country code and location name get lat & lon

                os.system('clear') # clear screen
                print(f"Location: {location_name} | Country Code: {country_code} ")        
                get_location_weather(lat, lon, api_key, settings["units"]) # use lat,lon, apikey and units saved to get weather

                save_location_answer = save_location_input()  # prompt user if they want to save location searched
                data = [today, location_name, country_code]  
                if save_location_answer == "Y":
                    print("✔ Location not saved.")
                    append_csv(data)  # saves  data to csv if y 
                else:
                    os.system('clear')
                    print("✘ Location not saved.")
                
                action = user_next_action(lat,lon, api_key) # message for next action 

                if action == "main_menu":
                    break

    # 2nd Sub-Menu =  Saved locations - saved locations module 
        if int(menu_user_input) == 2:
            os.system('clear')
            print_csv()   # get list of saved location 
            location_name2, country_code2 = selection()  

            os.system('clear')
            lat2,lon2 = get_lon_lat_location(location_name2, country_code2, api_key)
            print(f"Location: {location_name2} | Country Code: {country_code2} ")        
            get_location_weather(lat2, lon2, api_key, settings["units"])
            action = user_next_action(lat2,lon2, api_key)

    # 3rd Sub-Menu =  Get weather for any date and location
        if int(menu_user_input) == 3:
            os.system('clear')
            date_answer = date_input() # what date?
            country_code3 = get_country_code() # which country code?
            location_name3 = get_location_name(country_code3) # which location?
            lat3, lon3 = get_lon_lat_location(location_name3,country_code3,api_key) # get lat lon with openapi

            os.system('clear')
            specific_date(lat3, lon3, vc_api_key, date_answer) # feed lat, lon, api and dae into url
            input("\nPress Enter to go back to main menu...")


    # 4th Sub-Menu =  Settings
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
                change_units_menu(settings)
                settings_action = input("Enter 'h' to go back to the the main menu \t")
                if settings_action == 'h' :
                    continue


            if int(setting_user_input) == 2:
                os.system('clear')
                change_default(settings_default)
                if settings_action == 'h' :
                    continue

            if int(setting_user_input) == 3:
                break

    # Exit App
        if int(menu_user_input) == 5:
            sys.exit()



            

        


            





            
                
            

            




                        
                

            



            








        # if "cloud" in description:
        #     print("It's cloudy today.")
        # else:
        #     print("🌞 No clouds today!")

