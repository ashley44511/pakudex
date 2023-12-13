from pakuri import Pakuri

class Pakudex:
    def __init__(self, capacity=20):
        # default capacity is 20
        # initialize storing 0 pakuri
        self.capacity = capacity
        self.pakuris = []
        self.str_pakuris = []
        self.size = 0

    # getters
    def get_size(self):
        # return number of pakuri currently stored in pakudex
        return self.size

    def get_capacity(self):
        # return pakudex capacity
        return self.capacity

    def get_species_array(self):
        # string list containing species as ordered in pakudex
        # if no species, return none
        if self.size == 0:
            return None
        else:
            return self.str_pakuris

    def get_stats(self, species):
        # return int list containing stats of species at indices 0, 1, 2
        # if species not in pakudex, return None
        found = False
        for i in self.pakuris:
            if i.get_species() == species:
                # checks that pakuri exists. When pakuri is found, returns stats
                found = True
                # returns stats list
                return [i.get_attack(), i.get_defense(), i.get_speed()]
                break
        if found == False:
            # if pakuri isn't found, aka it doesn't exist, return None
            return None

    def sort_pakuri(self):
        # sort pakuri in pakudex according to python standard lexicographical ordering of species name
        self.str_pakuris.sort()

    def add_pakuri(self, species):
        # add species to pakudex
        # if successful, return True. if not, return False.
        success = True
        # checks that pakudex is below capacity
        if self.size >= self.capacity:
            success = False
        for i in self.pakuris:
            if i.get_species() == species:
                # checks that pakuri doesn't already exist in pakudex
                success = False
                break
        # if pakuri doesn't exist, adds pakuri by appending to self.pakuris list and updating self.size
        if success == True:
            self.pakuris.append(Pakuri(species))
            self.str_pakuris.append(species)
            self.size += 1
        return success

    def evolve_species(self, species):
        # attempts to evolve species in pakudex
        # if successful, return True. if not, return False.
        success = False
        for i in self.pakuris:
            if i.get_species() == species:
                # checks that pakuri exists
                success = True
                i.evolve()
                break
        return success


