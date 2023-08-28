# Favorite Cities lesson from Codedex

class City:
    def __init__(self, name, state, country, population, landmarks):
        self.name = name
        self.state = state
        self.country = country
        self.population = int(round(population, -3))
        self.landmarks = landmarks

nyc = City('New York', 'New York', 'United States of America', 8.468e6, ['Statue of Liberty', 'Empire State Building', 'Central Park', 'Chrysler Building', 'Flatiron Building'])

red = City('Redmond', 'Washington', 'United States of America', 76354, ['Redmond Town Center', 'Marymoore Park', 'Perrigo Park', 'Sammamish River Trail'])