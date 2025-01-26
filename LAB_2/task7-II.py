# overriding Example
class Animal:
    def Sound(self):
        print("Some Generic Sound")
class Dog(Animal):
    def Sound(self):
        print("Bark")
animal=Animal()
dog=Dog()
animal.Sound()
dog.Sound()
