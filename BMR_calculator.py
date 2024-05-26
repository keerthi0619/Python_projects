import math

print('''Hi Welcome to BMR Calculator
      Please answer the questions to find your maximum calorie intake''')

Gender=input("Please select your gender Male/Female")
Age=int(input("Enter your age in years"))
Weight=int(input("Enter your weight in kgs"))
Height=int(input("Enter your  height in cm"))

if(Gender=='Female'):
    BMR=(10*Weight) + (6.25*Height) - (5*Age) - 161
    print(f"Your Calorie intake should be below {BMR} calories")
else:
    BMR=(10*Weight) + (6.25*Height) - (5*Age) + 5
    print(f"Your Calorie intake should be below {BMR} calories")

print("Thankyou for choosing BMR today")



