# Making Nodes
class student_node:
    def __init__(self, name):
        self.name = name
        self.next = None

class Professor_node:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.student_head = None

class Department_treeNode:
    def __init__(self, name):
        self.name = name
        self.subDept = []  # List of child departments
        self.prof_head = None

# Global stack for recently added students
review_stack = []

# Adding Data
def insert(parent, dept_name):
    new_dept = Department_treeNode(dept_name)
    if parent:
        parent.subDept.append(new_dept)  # Append the OBJECT, not just name
    return new_dept

def add_prof(dept, prof_name):
    new_prof = Professor_node(prof_name)
    new_prof.next = dept.prof_head
    dept.prof_head = new_prof

def add_stud(prof, student_name):
    new_student = student_node(student_name)
    new_student.next = prof.student_head
    prof.student_head = new_student
    review_stack.append(new_student)  # Push student object to stack

# Display Structure
def display(dept, indent=" "):
    print(indent + "Department:", dept.name)
    prof = dept.prof_head
    while prof:
        print(indent + " Professor:", prof.name)
        stu = prof.student_head
        while stu:
            print(indent + "   Student:", stu.name)
            stu = stu.next
        prof = prof.next
    for sub_dept in dept.subDept:
        display(sub_dept, indent + "  ")

# Show Recently Added Students
def show_recent_students(N):
    print(f"\nTop {N} Recent Students:")
    for student in reversed(review_stack[-N:]):
        print(student.name)


# Create Root Department
root = insert(None, "University")

# Add Sub Departments
comp = insert(root, "Computer Science")
sow = insert(root, "Software Department")

# Add Professors
add_prof(comp, "Dr. Ali")
add_prof(comp, "Dr. Sara")
add_prof(sow, "Dr. Sana")
add_prof(sow, "Dr. Saleem")

# Add Students
add_stud(comp.prof_head, "Areeba")             # To Dr. Sara
add_stud(comp.prof_head.next, "Usman")         # To Dr. Ali
add_stud(sow.prof_head, "Aliya")               # To Dr. Saleem
add_stud(sow.prof_head.next, "Zainab")         # To Dr. Sana

# Display Full Structure
display(root)

# Show Top 3 Recently Added Students
show_recent_students(3)
