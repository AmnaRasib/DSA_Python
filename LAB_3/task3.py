# Student Grade Tracker
class GradeTracker:
    def __init__(self):
        self.grades=[]
    def addGrades(self,grade):
        return self.grades.append(grade)
    def avg_Grade(self):
        return sum(self.grades)/len(self.grades) if self.grades else 0
    def highest_Grade(self):
        return max(self.grades) if self.grades else 0
    def lowest_Grade(self):
        return min(self.grades) if self.grades else 0
g=GradeTracker()
g.addGrades(78)
g.addGrades(89)
g.addGrades(90)
print("Average: ",g.avg_Grade())
print("Highest Grade: ",g.highest_Grade())
print("Lowest Grade: ",g.lowest_Grade())

    
    