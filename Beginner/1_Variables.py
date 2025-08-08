# 1. Create a variable named pi and store the value 22/7 in it. Now check the data type of this variable.

pi = 22/7
print(type(pi)) # Output: <class 'float'>
print("-----------------------------------------------------------------------------------------")


# 2. Create a variable called for and assign it a value 4. See what happens and find out the reason behind the behavior that you see.
# for = 4 => there is a syntax error because 'for' is a reserved keyword in Python.


# 3. Store the principal amount, rate of interest, and time in different variables and then calculate the Simple Interest for 3 years. Formula: Simple Interest = P x R x T / 100

principal = float(input("Enter the principal amount: ")) #15000
rate_of_interest = float(input("Enter the rate of interest: ")) # 10
time = float(input("Enter the time in years : "))  # 3
simple_interest = (principal * rate_of_interest * time) / 100
print("Simple interest for " , time ," years is:", simple_interest) # Output: Simple interest for 3 years is: 4500.00

