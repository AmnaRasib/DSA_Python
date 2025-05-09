class StudentNode:
    def __init__(self,name,application_id,score):
        self.name=name
        self.application_id=application_id
        self.score=score
        self.right=None
        self.left=None
def save_student_to_file(name,application_id,score):
     with open("students_data.txt","a") as file:
          file.write(f"Name: {name}, ID: {application_id}, Score: {score}\n")
def insert(root,name,application_id,score):
        if root is None:
            save_student_to_file(name,application_id,score)
            print(f"Saved student: {name}, ID: {application_id}, Score: {score}")
            return StudentNode(name,application_id,score)
        if score < root.score:
            root.left=insert(root.left,name,application_id,score)
        elif score > root.score:
            root.right= insert(root.right,name,application_id,score)
        else:
            print(f"Duplicate score {score} not allowed!")
        return root
def inorder(root):
     if root:
          inorder(root.left)
          print(f"Name: {root.name}, ID: {root.application_id}, Score: {root.score}")
          inorder(root.right)
def search(root,score):
     if root is None:
          return None
     if score == root.score:
          return root
     elif score< root.score:
          return search(root.left,score)
     else:
          return search(root.right,score)
def print_range(root,x,y):
     if not root:
          return
     if x < root.score:
          print_range(root.left,x,y)
     if x<= root.score <=y:
          print(f"Name: {root.name}, ID: {root.application_id}, Score: {root.score}")
     if y > root.score:
          print_range(root.right,x,y)
def count_less(root,score):
     if root is None:
          return 0
     if root.score < score:
          return 1+count_less(root.left,score) + count_less(root.right,score)
     else:
          return count_less(root.left,score)
if __name__ == "__main__":
     root=None
     while True:
          print("\n*****Welcome to Student Ranking System*****")
          print("1. Insert Student")
          print("2. Print All Students")
          print("3. Search Students by Score")
          print("4. Print Students in Score Range.")
          print("5. Rank of Student")
          print("6. Exit")

          choice=int(input("Enter your choice: "))
          if choice==1:
               name= input("Enter student name: ")
               app_id=input("Enter application_id: ")
               score=int(input("Enter admission score: "))
               root= insert(root,name,app_id,score)
          elif choice==2:
               print("\n---Students in Ascending order of Scores---")
               inorder(root)
          elif choice==3:
               score=int(input("Enter Score to Search: "))
               student=search(root,score)
               if student:
                    print(f"Found: Name: {student.name}, ID: {student.application_id}, Score: {student.score}")
               else:
                    print("Student not found!")
          elif choice==4:
               x=int(input("Enter Lower bound Score: "))
               y=int(input("Enter upper bound score:"))
               print(f"\n---Student with scores between {x} and {y}---")
               print_range(root,x,y)
          elif choice==5:
               score=int(input("Enter the score to find rank: "))
               rank=count_less(root,score)
               print(f"Number of Students who scored less than {score}: {rank}")
          elif choice==6:
               print("Exiting the program. GOODBYE :)")
               break
          else:
               print("Invalid choice. Please try again.")

