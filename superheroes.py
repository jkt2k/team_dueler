import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name=name
        self.attack_strength=attack_strength
    def attack(self):
        return random.randint(0,self.attack_strength)
class Armor:
    def __init__(self, name, max_block):
        self.name=name
        self.max_block=max_block
    def block(self):
        return random.randint(0,self.max_block)
class Hero:
    def __init__(self, name, starting_health=100):
        self.name=name
        self.current_health=starting_health
        self.starting_health=starting_health
        self.abilities=[]
        self.armors=[]
        self.deaths = 0
        self.kills = 0
    def add_ability(self, ability):
        self.abilities.append(ability)
    def attack(self):
        attack_sum=0
        for ability in self.abilities:
            attack_sum+=ability.attack()
        return attack_sum
    def add_armor(self, armor):
        self.armors.append(armor)
    def armor(self):
        armor_sum=0
        for armor in self.armors:
            armor_sum=armor_sum+armor.block()
        return armor_sum
    def defend(self):
        if len(self.armors)==0:
            return 0
        else:
            block_sum=0
            for armor in self.armors:
                block_sum+=armor.block()
            return block_sum
    def take_damage(self, damage):
        if damage>=0:
            self.current_health-=(damage-self.defend())
    def is_alive(self):
        if self.current_health<=0:
            return False
        else:
            return True
    def fight(self,opponent):
        if len(self.abilities)==0 and len(opponent.abilities)==0:
            print("Draw")
        else:
            opponent.take_damage(self.attack()-opponent.defend())
            if not opponent.is_alive():
                self.add_kills(1)
                opponent.add_deaths(1)
                print(self.name+" defeats "+opponent.name+".")
            else:
                opponent.fight(self)
    def add_kills(self,num_kills):
        self.kills+=num_kills
    def add_deaths(self,num_deaths):
        self.deaths+=num_deaths
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
class Weapon(Ability):
    def attack(self):
        return random.randint(self.attack_strength//2,self.attack_strength)

class Team():
    def __init__(self,name):
        self.name=name
        self.heroes=[]
    def add_hero(self,hero):
        self.heroes.append(hero)
    def remove_hero(self,hero):
        for i, hero in enumerate(self.heroes):
            self.heroes.pop(i)
        else:
            return 0
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
    def attack(self, other_team):
        if len(self.heroes)==0 and len(other_team.heroes)==0:
            print("Draw")
        else:
            attack_over=False
            abilities_present=False
            while attack_over==False:
                friendly_roster=[]
                enemy_roster=[]
                for hero in self.heroes:
                    if hero.is_alive():
                        friendly_roster.append(hero)
                    if len(hero.abilities)!=0:
                        abilities_present=True
                for hero in other_team.heroes:
                    if hero.is_alive():
                        enemy_roster.append(hero)
                    if len(hero.abilities)!=0:
                        abilities_present=True
                if len(friendly_roster)==0:
                    attack_over=True
                    print(other_team.name+" wins the battle!")
                elif len(enemy_roster)==0:
                    attack_over=True
                    print(self.name+" wins the battle!")
                elif abilities_present==False:
                    attack_over=True
                    print("Draw.")
                else:
                    friendly_hero=friendly_roster[random.randint(0,len(friendly_roster)-1)]
                    enemy_hero=enemy_roster[random.randint(0,len(enemy_roster)-1)]
                    friendly_hero.fight(enemy_hero)
    def revive_heroes(self, health=100):
        if len(self.heroes)!=0:
            for hero in self.heroes:
                hero.current_health=hero.starting_health

    def stats(self):
        if len(self.heroes)!=0:
            print("=== Stats for "+self.name+" ===")
            for hero in self.heroes:
                if hero.deaths!=0:
                    print(hero.name+": "+str(hero.kills/hero.deaths)+" KD ("+str(hero.kills)+"/"+str(hero.deaths)+")")
                elif hero.kills==0:
                    print(hero.name+": 0 KD (0/0)")
                else:
                    print(hero.name+": Perfect KD ("+str(hero.kills)+"/0)")

class Arena:
    def __init__(self):
        self.team_one=Team("Team one")
        self.team_two=Team("Team two")
    def create_ability(self):
        ability_name=input("Enter ability name: ")
        ability_strength=int(input("Enter ability strength: "))
        return Ability(ability_name,ability_strength)
    def create_weapon(self):
        weapon_name=input("Enter weapon name: ")
        weapon_strength=int(input("Enter weapon strength: "))
        return Weapon(weapon_name,weapon_strength)
    def create_armor(self):
        armor_name=input("Enter armor name: ")
        armor_strength=int(input("Enter armor block amount: "))
        return Armor(armor_name,armor_strength)
    def create_hero(self):
        hero_name=input("Enter hero name: ")
        hero_starting_health=int(input("Enter hero starting health: "))
        temp_hero=Hero(hero_name,hero_starting_health)
        creating_armors=True
        while creating_armors:
            create_armor=input("Add armor? ")
            if create_armor[0]=="y" or create_armor[0]=="Y":
                temp_hero.add_armor(self.create_armor())
            else:
                creating_armors=False
        creating_weapons=True
        while creating_weapons:
            create_weapon=input("Add weapon? ")
            if create_weapon[0]=="y" or create_weapon[0]=="Y":
                temp_hero.add_weapon(self.create_weapon())
            else:
                creating_weapons=False
        creating_abilities=True
        while creating_abilities:
            create_ability=input("Add ability? ")
            if create_ability[0]=="y" or create_ability[0]=="Y":
                temp_hero.add_ability(self.create_ability())
            else:
                creating_abilities=False
        return temp_hero
    def build_team_one(self):
        hero_amt=int(input("How many heroes do you want to add to team 1?"))
        for i in range(0,hero_amt):
            self.team_one.add_hero(self.create_hero())
    def build_team_two(self):
        hero_amt=int(input("How many heroes do you want to add to team 2?"))
        for i in range(0,hero_amt):
            self.team_two.add_hero(self.create_hero())
    def team_battle(self):
        print("=== BATTLE BEGINS ===")
        self.team_one.attack(self.team_two)
    def show_stats(self):
        self.team_one.stats()
        self.team_two.stats()

if __name__ == "__main__":
    game_is_running = True
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")
        if play_again.lower() == "n":
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()