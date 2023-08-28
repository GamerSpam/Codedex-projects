# Pokedex lesson from Codedex

class Pokemon:
    def __init__(self, entry : int, name : str, type : list, description : str, is_caught : bool):
        self.entry = entry
        self.name = name
        self.type = type
        self.description = description
        self.is_caught = is_caught

    def speak(self):
       return self.name

pika = Pokemon(25, 'Pikachu', ['Electiric'], 'When it is angered, it immediately discharges the energy stored in the pouches in its cheeks.', False)

duo = Pokemon(578, 'Duosion', ['Psychic'], 'Its psychic power can supposedly cover a range of more than half a mile—but only if its two brains can agree with each other.', False)

pid = Pokemon(18, 'Pidgeot', ['Normal', 'Flying'], 'This Pokémon flies at Mach 2 speed, seeking prey. Its large talons are feared as wicked weapons.', False)

print(pika.speak())
print(duo.speak())
print(pid.speak())