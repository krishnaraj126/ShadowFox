Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input("Enter the name for the first city : ")
city2 = input("Enter the name for the second city : ")

def get_country(city):
    if city in Australia:
        return "Australia"
    elif city in UAE:
        return "UAE"
    elif city in India:
        return "India"
    else:
        return None

country1 = get_country(city1)
country2 = get_country(city2)

if country1 is None or country2 is None:
    print("One or both cities are not in the list")
elif country1 == country2:
    print(f"Both cities are in {country1}")
else:
    print("They dont belong to the same country")
    