# ### Problem 10:
# Create a new empty array called pet_list. Create a Pet class with a type and breed attribute/property. Include a method that will print each attribute/property. Add 3 pet objects to the pet_list array. Print the attributes/properties for each pet.

class Pet:
    def __init__(self, type, breed):
        self.type = type
        self.breed = breed

    def printAllAttributes[self]:
        print(F"The type is: {self.type}. The breed is: {self.breed}")

emptyArray = []
pet1 = Pet("Dog", "Bulldog")
pet2 = Pet("Cat", "Persian")
pet3 = Pet("Bird", "Canary")

emptyArray.append(pet1)
emptyArray.append(pet2)
emptyArray.append(pet3)

for eachElement in emptyArray:
    eachElement.printAllAttributes()