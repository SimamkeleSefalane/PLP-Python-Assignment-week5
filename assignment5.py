# Base class
class Superhero:
    def __init__(self, name, alias, power):
        self.name = name
        self.alias = alias
        self.power = power

    def introduce(self):
        return f"I am {self.alias}, real name {self.name}."

    def attack(self):
        return f"{self.alias} attacks with basic powers! Power: {self.power}"


# Inherited class: TechHero
class TechHero(Superhero):
    def attack(self):
        return f"{self.alias} attacks with high-tech gadgets! Power: {self.power}"


# Inherited class: MutantHero
class MutantHero(Superhero):
    def attack(self):
        return f"{self.alias} uses mutant abilities! Power: {self.power}"


# Create hero objects
hero1 = TechHero("Lebo Maseko", "Cyber Falcon", 80)
hero2 = MutantHero("Zanele Duma", "Mind Blaze", 90)

# Show results
print(hero1.introduce())
print(hero1.attack())

print(hero2.introduce())
print(hero2.attack())
