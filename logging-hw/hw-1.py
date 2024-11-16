import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log",
                    filemode="w",
                    format="We have next logging message:%(asctime)s:%(levelname)s - %(message)s"
                    )
class Animal:
    def __init__(self, weight = 96, height = 110, width = 65, length = 140, age = 5):
        self.weight = weight
        self.height = height
        self.width = width
        self.length = length
        self.age = age
        logging.debug(f"Animal created with parameters: weight: {self.weight}, height: {self.height}, width: {self.width}, length: {self.length}, age: {self.age}")


    def animal_info(self):
        info = (f"Weight: {self.weight}, height: {self.height}, width: {self.width}, length: {self.length}, age: {self.age}")
        print(info)
        logging.debug(f"Animal info displayed: {info}")

Animal = Animal()
Animal.animal_info()


