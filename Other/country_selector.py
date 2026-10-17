def linear_sorted(countries, country):
    index = 0


    while index < len(countries) and countries[index].lower() != country and countries[index].lower() < country:
        index += 1

    if index < len(countries) and countries[index].lower() == country:
       return index
    else:
        return -1

countries = []
try:
    with open("countries.txt") as f:
        countries = f.read().splitlines()  
    print(countries)  

except FileNotFoundError:
    print("Error: The file 'countries.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

country = input("State the Country: ").lower()
result = linear_sorted(countries, country)

if result != -1:
    print(f"{country}, spotted")
else:
    print(f"{country}, not spotted")
