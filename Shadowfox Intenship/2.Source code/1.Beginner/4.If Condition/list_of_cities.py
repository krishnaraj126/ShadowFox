Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]

city = input("Enter the name of the city :")

if city in Australia:
    print(city,"in Australia")
elif city in UAE:
    print(city,"in UAE")
elif city in India:
    print(city,"in India")
else:
    print("City not in List")