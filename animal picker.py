import random
animals = ["dog", "cat", "horse"]
listLength = len(animals)

animalChoice = random.randint(0, listLength)
theAnimal = animals[animalChoice]
print(theAnimal, animalChoice)

class Dog:
    def __init__(self, name, age) -> None:
        
        