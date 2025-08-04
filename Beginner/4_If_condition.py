#1. Write a program to determine the BMI Category based on user input.Ask the user to: Enter height in meters , Enter weight in kilograms , Calculate BMI using the formula: BMI = weight / (height)2
#Use the following categories:
#If BMI is 30 or greater, print "Obesity"
#If BMI is between 25 and 29, print "Overweight"
#If BMI is between 18.5 and 25, print "Normal"
#If BMI is less than 18.5, print "Underweight"
#Example:Enter height in meters: 1.75 , Enter weight in kilograms: 70 , Output: "Normal"

height = float(input("Enter height in meters: ")) # 1.8
weight = float(input("Enter weight in kilograms: ")) # 79
bmi = weight / (height ** 2) 
print("Your BMI is:", bmi)  # Output: Your BMI is: 24.382716049382715  
if(bmi >= 30):
    print("Obesity")
elif(bmi >= 25):
    print("Overweight") 
elif(bmi >= 18.5):
    print("Normal")
else:
    print("Underweight")
    
print("-------------------------------------------------------------------------")

# 2. Write a program to determine which country a city belongs to. Given list of cities per country:
# Australia = ["Sydney","Melbourne","Brisbane","Perth"]
# UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
# India = ["Mumbai","Bangalore","Chennai","Delhi"]
#Ask the user to enter a city name and print the corresponding country.
#Example:Enter a city name: "Abu Dhabi"
#Output: "Abu Dhabi is in UAE"

australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]    
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
city = input("Enter a city name: ")  # Mumbai
if city in australia:
    print( city , "is in Australia")
elif city in uae:
    print( city ,"is in UAE")
elif city in india:
    print( city ,"is in India")
print("-------------------------------------------------------------------------")

# 3. Write a program to check if two cities belong to the same country. Ask the user to enter two cities and print whether they belong to the same country or not.
#Example: Enter the first city: "Mumbai"
#    Enter the second city: "Chennai"
#    Output: "Both cities are in India"
#Example: Enter the first city: "Sydney"
#   Enter the second city: "Dubai"
#   Output: "They don't belong to the same country"

city1 = input("Enter the first city: ")  # Mumbai
city2 = input("Enter the second city: ")  # Dubai

if city1 in australia and city2 in australia:
    print("Both cities are in Australia")
elif city1 in uae and city2 in uae:
    print("Both cities are in UAE") 
elif city1 in india and city2 in india:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")   
