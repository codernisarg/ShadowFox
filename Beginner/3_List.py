#1. You have a list of superheroes representing the JusticeLeague. justice_league = ["Superman","Batman","WonderWoman","Flash","Aquaman","Green Lantern"]
justice_league = ["Superman", "Batman", "WonderWoman", "Flash", "Aquaman", "Green Lantern"]
print("Justice League Members:", justice_league)  # Output: Justice League Members: ['Superman', 'Batman', 'WonderWoman', 'Flash', 'Aquaman', 'Green Lantern']
print("-------------------------------------------------------------------------")

# Perform the following tasks: 
# 1. Calculate the number of members in the Justice League.
total_members = len(justice_league)
print("Total Members in Justice League:", total_members)  # Output: Total Members in Justice League: 6
print("-------------------------------------------------------------------------")

# 2. Batman recruited Batgirl and Nightwing as new members. Add them to your list.
justice_league.extend(["Batgirl", "Nightwing"])
print("Updated Justice League Members:", justice_league)  # Output: Updated Justice League Members: ['Superman', 'Batman', 'WonderWoman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']
print("-------------------------------------------------------------------------")

# 3. Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list.
justice_league.remove("WonderWoman")
justice_league.insert(0, "WonderWoman") 
print("Justice League Members after moving WonderWoman to the beginning:", justice_league)  # Output: Justice League Members after moving WonderWoman to the beginning: ['WonderWoman', 'Superman', 'Batman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']
print("-------------------------------------------------------------------------")

# 4. Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or "Superman" and move them in between Aquaman and Flash
flash_index = justice_league.index("Flash")
aquaman_index = justice_league.index("Aquaman")

if aquaman_index < flash_index:
    insert_index = aquaman_index
else:
    insert_index = flash_index

justice_league.remove("Superman")
justice_league.insert(insert_index, "Superman")
print("Justice League Members after conflict between aquaman and flash : ", justice_league) #Justice League Members after conflict between aquaman and flash :  ['WonderWoman', 'Batman', 'Flash', 'Superman', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']
print("-------------------------------------------------------------------------")


# 5. The Justice League faced a crisis, and Superman decided to assemble a new team. Replace the existing list with the following new members: "Cyborg","Shazam","Hawkgirl","MartianManhunter","Green Arrow".

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "MartianManhunter", "Green Arrow"]
print("New Justice League Members:", justice_league)  # Output: New Justice League Members: ['Cyborg', 'Shazam', 'Hawkgirl', 'MartianManhunter', 'Green Arrow']
print("-------------------------------------------------------------------------")

# 6. Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.
justice_league.sort()
print("Sorted Justice League Members:", justice_league)  # Output: Sorted Justice League Members: ['Cyborg', 'Green Arrow', 'Hawkgirl', 'MartianManhunter', 'Shazam']
print("-------------------------------------------------------------------------")

#Bonus: Print the new leader of the Justice League.
print("New Leader of Justice League:", justice_league[0])  # Output: New Leader of Justice League: Cyborg