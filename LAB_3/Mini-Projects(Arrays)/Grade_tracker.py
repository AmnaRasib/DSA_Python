class GradeTracker:
    def __init__(self):
        self.grades=[]
    def add_GradeInfo(self):
        num=int(input("Enter Number of Students: "))
        for i in range (num):
            x=int(input(f"Enter the Grade of Student {i+1}: "))
            self.grades.append(x)
        for j, grade in enumerate(self.grades,1):
            print(f"Student-{j}: {grade} ")
    def  Avg_grade(self):
        return sum(self.grades)/len(self.grades) if self.grades else 0
    def maxGrade(self):
        return max(self.grades) if self.grades else 0
    def minGrade(self):
        return min(self.grades) if self.grades else 0
    def gradesAboveAverage(self):
       avg= self.Avg_grade()
       print(f"\nGrades Greater than or equal to the average {avg}: ")
       for grade in self.grades:
           if grade>=avg:
               print(grade, end=" ")
g=GradeTracker()
g.add_GradeInfo()
print("\nAverage Grade: ",g.Avg_grade())
print("Maximum Grade is: ",g.maxGrade())
print("Minimum Grade is: ",g.minGrade())
g.gradesAboveAverage()