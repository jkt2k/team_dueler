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
                print(self.name+" wins!")
            else:
                opponent.fight(self)
class Weapon(Ability):
    def attack(self):
        return random.randint(self.attack_strength/2,self.attack_strength)

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman", 100)
    hero2 = Hero("Dumbledore", 100)
    ability1 = Ability("Super Speed", 50)
    ability2 = Ability("Super Eyes", 50)
    ability3 = Ability("Wizard Wand", 50)
    ability4 = Ability("Wizard Beard", 50)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)