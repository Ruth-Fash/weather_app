
openweather_langs = {
    "zh_tw": "Chinese Traditional", "nl": "Dutch", "en": "English", "fr": "French", "de": "German", 
    "el": "Greek", "hi": "Hindi", "it": "Italian", "ja": "Japanese", "kr": "Korean", "pl": "Polish", 
    "pt": "Portuguese", "ru": "Russian", "sr": "Serbian", "es": "Spanish", "ua": "Ukrainian"
}

def select_langauge():
    try:

        lang_list = list(openweather_langs.items())  # Convert dict to list of tuples
        for index, (code, name) in enumerate(lang_list):  # Start at 1
            print(f"{index}. {name} ({code})")

        while True:
            user_input = input("Select a langauge index:")

            if not user_input:
                print("No language selected. Defaulting to English.")        
                return "en"
            
            language_index = int(user_input)

            if 0 <= language_index < len(lang_list):
                selected_code = lang_list[language_index][0]  # Get language code
                return selected_code
            else:
                print("Invalid index. Please choose a number from the list.")

            
    except ValueError:
        print("Invalid index: Please enter a number")





    











