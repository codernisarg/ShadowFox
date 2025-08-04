#1. Write a function that takes two arguments, 145 and 'o', and uses the `format` function to return a formatted string. Print the result. Try to identify the representation used.

def format_value(value, representation):
    result = format(value, representation)
    return f"Formatted value of {value} in '{representation}' representation is: {result}"
answer = format_value(145, 'o') 
print(answer) #Output: Formatted value of 145 in 'o' representation is: 221

#In a village, there is a circular pond with a radius of 84 meters. Calculate the area of the pond using the formula: Circle Area = π * r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly 1.4 liters of water in a square meter, what is the total amount of water in the pond? Print the answer without any decimal point in it. Hint: Circle Area = π r^2 Water in the pond = Pond Area Water per Square Meter

def calculate_area(radius):
    return 3.14 * radius ** 2

def calculate_pond_water(radius, pi=3.14, water_per_sqm=1.4):
    area = calculate_area(radius)
    total_water = area * water_per_sqm
    return int(total_water)


radius = 84
area = calculate_area(radius) 
pond_water_calulation = calculate_pond_water(radius)
print("Area of the pond :", area) # Output: Area of the pond : 2208.96
print("Total amount of water in the pond (in liters):", pond_water_calulation)# Output: Total amount of water in the pond (in liters): 3092

#If you cross a 490 meterlong street in 7 minutes, calculate your speed in meters per second. Print the answer without any decimal point in it. Hint: Speed = Distance / Time
def calculate_speed(distance, time_minutes):
    time_seconds = time_minutes * 60  # Convert minutes to seconds
    speed = distance / time_seconds
    return int(speed)

distance = 490
time_minutes = 7
speed = calculate_speed(distance, time_minutes)
print("Speed in meters per second:", speed) # Output: Speed in meters per second: 1