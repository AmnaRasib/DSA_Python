# To-Do List Application
class ToDoList:
    def __init__(self):
        self.tasks=[]
        self.statuss=[]
    def addTask(self,task,status):
        self.tasks.append(task)
        self.statuss.append(status)
        if task in self.tasks: 
            self.tasks.remove(task)
        else:
            print(f"Task '{task}' not found") # f is formated String Literal
    def viewTasks(self):
        print("Tasks: ")
        for i, task in enumerate(self.tasks,1):
            print(f"{i}.{task}") 
        
    def viewStatus(self):
        print("Checked: ")
        for j,status in enumerate(self.statuss,1):
              print(f"{j}.{status}") 

to_do=ToDoList()
to_do.addTask("Buy Groceries",True)
to_do.addTask("Complete Hometask",False)
to_do.viewTasks()
to_do.viewStatus()





