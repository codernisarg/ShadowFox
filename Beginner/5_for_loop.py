# 1. 1. Using a for loop, simulate rolling a sixsided die multiple times (at least 20 times). Count and print the following statistics: How many times you rolled a 6 , How many times you rolled a 1 , How many times you rolled two 6s in a row

import random
num_rolls = int(input("Enter the number of times to roll the die (Minimum 20 times): "))  
rolls = []
six = 0
one = 0
two_six_in_row = 0

previous_roll = 0

for i in range(num_rolls):
    roll = random.randint(1, 6) # randint is used for Generate a random number 
    rolls.append(roll)

    if roll == 6:
        six += 1
    if roll == 1:
        one += 1
    if previous_roll == 6 and roll == 6:
        two_six_in_row += 1

    previous_roll = roll  # Update for next loop

print("Die rolls:", rolls)
print("Number of times 6 was rolled:", six)
print("Number of times 1 was rolled:", one)
print("Number of times two 6s were rolled in a row:", two_six_in_row)
print("-------------------------------------------------------------------------")


# 2. Imagine you are doing a workout routine, and you have to complete 100 jumping jacks. Write a program that: Asks you to perform 10 jumping jacks at a time. After each set, it asks, "Are you tired?"
#If you reply "yes" or "y," it should ask if you want to skip the remaining sets.
#If you reply "yes" or "y," it should break and print, "You completed a total of jumping jacks."
# For example, if you did only 30 jumping jacks and answered "yes," the program will break and print, "You completed a total of 30 jumping jacks."
#If you reply "no" or "n," it should continue and display how many jumping jacks are remaining. After that, ask you again, "Are you tired?"
# For example, if you answered "no," it should display that 70 jumping jacks are remaining and ask you again, "Are you tired?"
# If you reply "no" or "n," it should continue and display how many jumping jacks are remaining. After that, ask you again, "Are you tired?" 
# For example, if you answered "no," it should display that 70 jumping jacks are remaining and ask you again, "Are you tired?" 
# If you complete all 100 jumping jacks, it should print, "Congratulations! You completed the workout," and stop the program

total_jumping_jacks = 100
set_size = 10
completed = 0

for i in range(1, (total_jumping_jacks // set_size) + 1):
    completed += set_size
    print("You completed ", completed ,"jumping jacks.")

    if completed == total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/no): ").strip().lower()

    if tired in ['yes', 'y']:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
        if skip in ['yes', 'y']:
            print("You completed a total of ", completed ,"jumping jacks.")
            break
        else:
            remaining = total_jumping_jacks - completed
            print(remaining ,"jumping jacks remaining. Keep going!")
    elif tired in ['no', 'n']:
        remaining = total_jumping_jacks - completed
        print(remaining ,"jumping jacks remaining. Keep going! ")
    else:
        print("Invalid input. Assuming you're not tired. Continuing...")
        remaining = total_jumping_jacks - completed
        print(remaining ,"jumping jacks remaining. Keep going!")
