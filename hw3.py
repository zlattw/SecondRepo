class Animal:
    def __init__(self, weight = 96, height = 110, width = 65, length = 140, age = 5):
        self.weight = weight
        self.height = height
        self.width = width
        self.length = length
        self.age = age

    def animal_info(self):
        print(f"Weight: {self.weight}, height: {self.height}, width: {self.width}, length: {self.length}, age: {self.age}")

Animal = Animal()
Animal.animal_info()