weight_kg = float(input("Enter your weight (kg): "))
height_m = float(input("Enter your height (m): "))
bmi = weight_kg / (height_m ** 2)
if bmi < 16:
    print ("SEVERE THINNESS")
elif bmi < 17: 
   print ("MODERATE THINNESS")
elif bmi < 18.5:
    print ("MILD THINNESS")
elif bmi < 25:
    print ("NORMAL")
elif bmi < 30:
    print ("OVERWEIGHT")
elif bmi < 35:
    print ("OBESE CLASS 1")
elif bmi < 40:
   print ("OBESE CLASS 2")
else:
    print ("OBESE CLASS 3")
