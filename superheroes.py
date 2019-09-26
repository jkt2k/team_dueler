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
        self.abilities=[]
        self.armors=[]
    def add_ability(self, ability):
        self.abilities.append(ability)
    def attack(self):
        attack_sum=0
        for ability in self.abilities:
            attack_sum=attack_sum+ability.attack()
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
        self.current_health-=(damage-self.defend())
    

        

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    hey=Armor("heyyyy",20)
    hero.add_armor(hey)
    print(hero.attack())
    print(hero.armor())
    print(hero.defend())
    print(hero.current_health)
    hero.take_damage(50)
    print(hero.current_health)