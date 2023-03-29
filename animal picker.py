import random
animals = ["dog", "cat", "horse"]
listLength = (len(animals)) - 1

animalChoice = random.randint(0, listLength)
theAnimal = animals[animalChoice]
print(theAnimal, animalChoice)

dog = {
    "vertebrate": True
}

x = input()
if x == "vertebrate" or "Vertebrate" or "VERTEBRATE":
    print(dog["vertebrate"])