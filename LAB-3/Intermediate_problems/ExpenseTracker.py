class ExpenseTracker:
    def __init__(self):
        self.categories=["Food","Travel","Utilities"]
        self.expenses=[[] for _ in self.categories]

    def User_input(self):
        for i,category in enumerate(self.categories):
            num=int(input(f"How Many Expenses you want to enter for {category} : "))
            for j in range(num):
                expense=float(input(f"Enter Expense_{j+1} for {category}: "))
                self.expenses[i].append(expense)
    
    def Total_Expenses(self):
        total_expense=[]
        for expense_list in self.expenses:
            total=sum(expense_list)
            total_expense.append(total)
        print("\nTotal Expenses:")
        for i in range(len(self.categories)):
            print(f"{self.categories[i]}: {total_expense[i]}:.2f")

e=ExpenseTracker()
e.User_input()
e.Total_Expenses()

    