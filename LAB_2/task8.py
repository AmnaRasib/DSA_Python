# Abstraction Using Abstract Classes
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Reactangle(Shape):
  def __init__(self,length,width):
      self.__length=length
      self.__width=width
  def area(self):
      return self.__length*self.__width
  def perimeter(self):
      return 2*(self.__length+self.__width)
  
rec=Reactangle(10.5,6)
print("Area: ",rec.area())
print("perimeter: ",rec.perimeter())


      