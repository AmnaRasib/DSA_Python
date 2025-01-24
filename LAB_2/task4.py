class Student:
  def __init__(self,name,age):
      self.name=name
      self.age=age

  def display_info(self):
     print(f"Student Name: {self.name}\n Student(age): {self.age}")

student1= Student("AliYar",18)
student1.display_info()
student2= Student("Mehmed",19)
student2.display_info()
