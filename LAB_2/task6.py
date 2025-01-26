# Python Inheritance
class Vehicle:

    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model

    def display_info(self):
        print(f"Brand: {self.__brand}\nModel: {self.__model}")

class Car(Vehicle):

    def __init__(self, brand, model,doors):
        super().__init__(brand, model)
        self.__doors=doors

    def display_info(self):
         super().display_info()
         print(f"Doors:{self.__doors}")

car = Car("Toyota", "Corolla", 4)
car.display_info()


        