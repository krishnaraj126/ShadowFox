height_meter = float(input("Enter your Height in meters: "))
weight_kilos = float(input("Enter your Weight in Kilograms: "))
bmi = weight_kilos/(height_meter*height_meter)

if bmi >=30:
    print("Obesity")
elif 25<= bmi < 30:
    print("Over Weight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Under Weight")