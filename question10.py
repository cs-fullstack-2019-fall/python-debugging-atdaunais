# ### Problem 10:
# Create a new empty array called pet_list. Create a Pet class with a type and breed attribute/property. Include a method that will print each attribute/property. Add 3 pet objects to the pet_list array. Print the attributes/properties for each pet.


class Pet:
    def __init__(self, type, breed):
        self.type = type
        self.breed = breed

    def printAllAttributes(self):  # self attribute was set in brackets instead of parentheses
        print(F"The type is: {self.type}. The breed is: {self.breed}")


pet_list = []  # name of array was incorrect
pet1 = Pet("Dog", "Bulldog")
pet2 = Pet("Cat", "Persian")
pet3 = Pet("Bird", "Canary")

pet_list.append(pet1)
pet_list.append(pet2)
pet_list.append(pet3)

for eachElement in pet_list:
    eachElement.printAllAttributes()