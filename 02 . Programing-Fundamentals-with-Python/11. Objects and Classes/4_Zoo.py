class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammals":
            self.mammals.append(name)
        elif species == "fishes":
            self.fishes.append(name)
        elif species == "birds":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            species_name = self.mammals
            species_print = "Mammals"
        if species == "fish":
            species_name = self.fishes
            species_print = "Fishes"
        if species == "bird":
            species_name = self.birds
            species_print = "Birds"

        names = ", ".join(self.name)
        return f"{species_print} in {zoo_name}: {names}"

    def get_total(self):
        return f"Total animals: {self.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())
for _ in range(n):
    species, name = input().split(" ")
    zoo.add_animal(species, name)

species = input()

print(zoo.get_info(species))
print(zoo.get_total())
