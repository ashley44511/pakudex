class Pakuri:
    def __init__(self, species):
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

    #getters and setters
    #getters: retrieve value of an attribute
    def get_species(self):
        # gets species name
        return self.species

    def get_attack(self):
        # gets attack stat
        return self.attack

    def get_defense(self):
        # gets defense stat
        return self.defense

    def get_speed(self):
        # gets speed stat
        return self.speed

    #setters: set the value of a specific attribute
    def set_species(self, new_species):
        # sets a new species name
        self.species = new_species

    def set_attack(self, new_attack):
        # sets a new attack stat
        self.attack = new_attack

    def set_defense(self, new_defense):
        # sets a new defense stat
        self.defense = new_defense

    def set_speed(self, new_speed):
        # sets a new speed stat
        self.speed = new_speed


    def evolve(self):
        #evolves critter by doubling attack, quadruple defense, and triple the speed
        #update self. attack, self.defense, ect.
        self.attack = self.attack * 2
        self.defense = self.defense * 4
        self.speed = self.speed * 3

    def __str__(self):
        return f"{self.species}"
