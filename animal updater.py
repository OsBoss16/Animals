import json

animals = []
n = int(input("Enter amount of animals: "))

print("Now list the animals: ")

for i in range(0, n):
    ele = (input())
  
    animals.append(ele)

with open("animals.json", 'w') as f:
    json.dump(animals, f, indent=2) 

print(animals)