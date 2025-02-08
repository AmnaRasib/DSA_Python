class AttendanceTracker:
    def __init__(self):
        self.Employees=["Sara","Ali","Ahmed","Aliyar","Fatima"]
        self.days=[[] for _ in self.Employees]

    def User_Input(self):
        for idx, employee in enumerate(self.Employees):
            print("\n")
            for i in range(0,5):
                x= int(input(f"Enter the Attendance of {employee} for day_{i+1} 0/1: "))
                self.days[idx].append(x)
    
    def percentage(self):
        total_attendancePer=[]
        for days_list in self.days:
            total=sum(days_list)/5*100
            total_attendancePer.append(total)
        print("\nPercetage:")
        for i in range (len(self.Employees)):
            print(f"{self.Employees[i]}, Percentage:{total_attendancePer[i]:.2f}%")
a=AttendanceTracker()
a.User_Input()
a.percentage()


