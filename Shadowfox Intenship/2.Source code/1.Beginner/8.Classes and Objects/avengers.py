class Avengers:
    def __init__(self, name, age, gender, super_power, weapon, leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.leader = leader

    def get_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Super Power : {self.super_power}")
        print(f"Weapon : {self.weapon}")

    def is_leader(self):
        if self.leader:
            print(f"{self.name} is the leader of the Avengers!")
        else:
            print(f"{self.name} is not the leader of the Avengers.")

captain_america = Avengers("Captain America", 45, "Male", "Super Strength", "Shield", leader=True)
iron_man = Avengers("Iron Man", 48, "Male", "Technology", "Armor")
black_widow = Avengers("Black Widow", 35, "Female", "Superhuman", "Batons")
hulk = Avengers("Hulk", 49, "Male", "Unlimited Strength", "No Weapon")
thor = Avengers("Thor", 56, "Male", "Super Energy", "Mjölnir")
hawkeye = Avengers("Hawkeye", 38, "Male", "Fighting Skills", "Bow and Arrows")

avengers_list = [captain_america, iron_man, black_widow, hulk, thor, hawkeye]

for hero in avengers_list:
    print("-------------------")
    hero.get_info()
    hero.is_leader()