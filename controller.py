import model


class Commander:

    def __init__(self):
        self.db = model.AnimalDataBase()

    def addAnimal(self, name: str, date_fo_birth: str, species: int):
        self.db.add_pets_in_db(name, date_fo_birth, species)

    def printListCommand(self, species: int, name: str):
        animal = self.db.get_info(animals=species, name=name)
        print(animal)

    def trainPets(self, species: int, name: str, command: str):
        pets = self.db.getPet(species, name)
        pets.train_pets(command)
