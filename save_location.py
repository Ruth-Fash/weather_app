import csv

headers = ["Date Saved", "Location", "Country Code"]


def save_location_input():
    while True:
        user_input = input("Do you want me to remember this location for next time? Y/N ")

        if not user_input:
            print("Error: Please enter Y/N")
            continue
        return user_input.capitalize()
    
def create_csv():
    with open("saved_locations.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Only writing headers for now

    print("CSV file with headers created. Ready to add data later.")


def append_csv(data):
    # If the file exists, check for duplicates
    with open("saved_locations.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header if it exists
        for row in reader:
            if row[1] == data[1] and row[2] == data[2]:
                print("⚠ Location already exists...not updated.")
                return  # Exit early on duplicate
            
    # Else No duplicates, so append
    with open("saved_locations.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)
        print("✔ Location saved successfully.")


def print_csv():
    with open("saved_locations.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader, None)  # skip header

       # Print a nice header for the output
        print(f"{'No.':<4} {'Location':<20} {'Country Code':<12}")
        print("-" * 50)

        for index, row in enumerate(reader, 1):
            location = row[1] 
            country = row[2] 
            print(f"{index:<4} {location:<20} {country:<12}")


def selection():
    with open("saved_locations.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        locations = list(reader)  # skip header

        user_input = int(input("Please enter a location number ")) -1
        selected = locations[user_input]
        print(selected)

        return selected[1], selected[2]








    












