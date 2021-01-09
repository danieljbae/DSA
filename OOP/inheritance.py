class Animal:
    def __init__(self,name=None,species=None,habitat=None):
        self.name = name
        self.species = species
        self.habitat = habitat

    def printAnimal(self):
        print(self.name)

# Different ways of inhereting
class Bear(Animal):
    """
    inherits all attributes + methods from parent (Animal)
    """
    pass

class Dog(Animal):
    """
     __init__ overrides all of parent's methods and attributes
    """
    def __init__(self,name=None,furColor=None,species=None):            # override attribute: name
        self.name = name
        self.furColor = furColor
        self.species = species

    def printAnimal(self):                                              # override method: printAnimal()
        print(f"Dog type: {self.furColor} {self.name}")

class Breed(Dog):
    """
    .super() inherits all attributes + methods from parent (Dog)
    saves coding: as we can just code extra functionality and inherit the rest
    """
    def __init__ (self, name, furColor, species, breedType):
        super().__init__(name, furColor, species)
        self.breedType = breedType

    def printBreed(self):
        self.printAnimal()                                              # method + attributes: Inherted from Parent
        print(f"\t- Breed Type: {self.breedType} {self.name}")

def main():
    print("\nApproach 1:")
    a1 = Animal("bear","Mammal","land")
    a1.printAnimal()

    print("\nApproach 2:")
    b1 = Bear("bear","Mammal","land")
    b1.printAnimal()

    print("\nApproach 3:")
    d1 = Dog("Husky", "Black","Mammal")
    d2 = Dog("Retriever","Golden","Mammal")
    for dog in [d1,d2]: dog.printAnimal()

    print("\nApproach 4:")
    breed1 = Breed("Husky", "Black","Mammal", "Siberian")
    breed2 = Breed("Husky", "Black","Mammal", "Alaskan")
    for breed in [breed1,breed2]:
        # breed.printAnimal()
        breed.printBreed()                                              # method + attributes: specific to child








if __name__ == '__main__':
    main()

