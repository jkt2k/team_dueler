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
        if len(self.abilities)==0 and len(opponent.abilities==0):
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
    def add_armor(self, armor):
        self.armors.append(armor)
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
            while attack_over==False:
                friendly_roster=[]
                enemy_roster=[]
                for hero in self.heroes:
                    if hero.is_alive():
                        friendly_roster.append(hero)
                for hero in other_team.heroes:
                    if hero.is_alive():
                        enemy_roster.append(hero)
                if len(friendly_roster)==0:
                    attack_over=True
                    print(other_team.name+" wins the battle!")
                elif len(enemy_roster)==0:
                    attack_over=True
                    print(self.name+" wins the battle!")
                else:
                    friendly_hero=friendly_roster[random.randint(0,len(friendly_roster)-1)]
                    enemy_hero=enemy_roster[random.randint(0,len(enemy_roster)-1)]
                    friendly_hero.fight(enemy_hero)

    def revive_heroes(self, health=100):
        if len(self.heroes)!=0:
            for hero in self.heroes:
                hero.is_alive=True
                hero.health=hero.starting_health

    def stats(self):
        if len(self.heroes)!=0:
            print("=== Stats for "+self.name+" ===")
            for hero in self.heroes:
                print(hero.name+": "+hero.kills/hero.deaths+" KD")

# • Team Class 1. init: Parameters: name: String 2. addhero: Parameters: hero:String 3. removehero: Parameters name: String 4. viewallheroes: Parameters: None

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman", 100)
    hero2 = Hero("Dumbledore", 100)
    ability1 = Ability("Super Speed", 20)
    ability2 = Ability("Super Eyes", 20)
    ability3 = Ability("Wizard Wand", 900)
    ability4 = Ability("Wizard Beard", 900)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    team1=Team("One")
    team2=Team("Two")
    team1.add_hero(hero1)
    team2.add_hero(hero2)
    team1.attack(team2)