#1.Avengers is a Marvel’s American Superheroes team, Now you want to showcase your programming skills by representing the Avengers team using classes. Create a class called Avenger and create these six superheroes using this class.
#2. super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk", "Thor", "Hawkeye"]
#3. Your Avenger class should have these properties:
#    1. Name
#    2. Age
#    3. Gender
#    4. Super Power
#    5. Weapon
#4. Captain America has Super strength, Iron Man has Technology, Black Widow is superhuman, Hulk has Unlimited Strength, Thor has super Energy and Hawkeye has fighting skills as superpowers.
#5. Weapons: Shield, Armor, Batons, No Weapon for hulk, Mjölnir, Bow, and Arrows
#6. Create methods to get the information about each superhero
#7. Create a method is_leader() which will tell if the superhero is a leader or not.

class Avenger:
    def __init__(self ,Name , age , gender, superpower , weapon):
        self.Name = Name
        self.age = age
        self.gender = gender
        self.superpower = superpower
        self.weapon = weapon
        
    def get_info(self):
        print(f"Name: {self.Name}")
        print(f"Age: {self.age}")
        print(f"gender: {self.gender}")
        print(f"Super Power: {self.superpower}")
        print(f"Weapon: {self.weapon}")
        print("-" * 30)
    
    def is_leader(self):
        if self.Name == "Captain America":
            print(f"{self.Name} is the leader of the Avengers.")
            print("-" * 30)

# Creating Dictionary superhero
super_heroes = [
    Avenger("Captain America", 100, "Male", "Super Strength", "Shield"),
    Avenger("IronMan", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 49, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 41, "Male", "Fighting Skills", "Bow and Arrows")
]

for hero in super_heroes:
    hero.get_info()
    hero.is_leader()