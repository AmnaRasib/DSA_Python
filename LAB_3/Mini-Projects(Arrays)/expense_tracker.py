from array import *
class ExpenseTrcaker:
    def __init__(self):
        self.expense=[]
    def add_expense(self):
        for i in range(7):
            x=int(input(f"Enter the Expense of day {i+1}: "))
            self.expense.append(x)
    def total_expense(self):
        return sum(self.expense)
    def avg_Expense(self):
        return sum(self.expense)/len(self.expense) 
    def Max_expense(self):
        return max(self.expense) if self.expense else 0
    def Min_expense(self):
        return min(self.expense) if self.expense else 0
e=ExpenseTrcaker()
e.add_expense()
print("\n")
print("Your Total Expenses: ",e.total_expense())
print("Your Average Expenses: ",e.avg_Expense())
print("Maximum Expenses: ",e.Max_expense())
print("Maximum Expenses: ",e.Min_expense())


    