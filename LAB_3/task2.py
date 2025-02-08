# Expense Tracker
class ExpenseTracker:
 def __init__(self):
    self.expenses=[]
 def add_expense(self,amount):
    self.expenses.append(amount)
 def tot_expense(self):
    return sum(self.expenses)
 def max_expense(self):
    return max(self.expenses) if self.expenses else 0 #This checks if the expenses list is not empty.
 def min_expense(self):                                #else 0: If the expenses list is empty, it returns 0.
    return min(self.expenses) if self.expenses else 0
e=ExpenseTracker()
e.add_expense(20.5)
e.add_expense(100.75)
print("Total Expenses: ",e.tot_expense())
print("Maximum Expense: ",e.max_expense())
print("Minimum Expense: ",e.min_expense())

