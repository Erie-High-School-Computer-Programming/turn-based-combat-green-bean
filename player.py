import random 
class Player:
    def __init__(self, name, hp, move_list):
        """This method initializes the character
        It should give the character a name, attack, defense, and health stat
        It should also give the character a movelist"""
        self.name = name
        self.hp = hp
        self.move_list = move_list
        
    def attack(self, move, target):
        """This method should allow the character to attack another character using the 
        selected move. The move should deal damage to the target character"""

        if random.randint(0, 100) < self.move_list[move]["accuracy"]:
            warden.hp -= self.move_list["Heavens_Sword"]["damage"]
            print(f"{target.name} was hit")
        else:
            print("Attack missed")




        attack = self.move_list[move]
        target.hp -= attack["damage"]

        

         


    def display_stats(self):
        """This method should display the current health of the character"""
        pass





warden = Player("Warden",
                 1000,
                {
                "punch": {"damage": 15, "accuracy": 100},
                "World_Slash":{"damage": 45, "accuracy": 75},
                "Downfall_Ram": {"damage": 80, "accuracy": 50},
                "Lockdown": {"damage": 140, "accuracy":25}
                }
                )



angel = Player("Angel", 
               750, 
               {
                "Heavens_Sword": {"damage": 45, "accuracy": 90},
                "Divergence":{"damage": 60, "accuracy": 75},
                "Impel_Of_The_Gates": {"damage": 105, "accuracy": 45}
                }
                )

demon = Player("Demon",
                500,
                {
                "Slash": {"damage": 30, "accuracy": 95 },
                "Fire_Dagger": {"damage": 60, "accuracy": 75}
                }
                )

jacob = Player("Jacob",
                1500,
                {
                "Knights_Blade": {"damage": 75, "accuracy": 90},
                "Shining_Armour": {"healing": 250, "accuracy": 100},
                "Blades_Of_The_Gods": {"damage": 200, "accuracy": 45}
                }
                )




print(warden.hp)
angel.attack("Heavens_Sword", warden)
print(warden.hp)
angel.attack("Blades_Of_The_Gods", warden)
print(warden.hp)
