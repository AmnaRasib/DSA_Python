# Node class for a Student
class StudentNode:
    def __init__(self, name, application_id, score):
        self.name = name
        self.application_id = application_id
        self.score = score
        self.left = None
        self.right = None

# Insert a new student node
def insert(root, name, application_id, score):
    if root is None:
        return StudentNode(name, application_id, score)
    if score < root.score:
        root.left = insert(root.left, name, application_id, score)
    elif score > root.score:
        root.right = insert(root.right, name, application_id, score)
    else:
        print(f"Duplicate score {score} not allowed!")
    return root

# In-order traversal (ascending order of scores)
def inorder(root):
    if root:
        inorder(root.left)
        print(f"Name: {root.name}, ID: {root.application_id}, Score: {root.score}")
        inorder(root.right)

# Search for a student by score
def search(root, score):
    if root is None:
        return None
    if score == root.score:
        return root
    elif score < root.score:
        return search(root.left, score)
    else:
        return search(root.right, score)

# Print students within a score range
def print_range(root, x, y):
    if not root:
        return
    if x < root.score:
        print_range(root.left, x, y)
    if x <= root.score <= y:
        print(f"Name: {root.name}, ID: {root.application_id}, Score: {root.score}")
    if y > root.score:
        print_range(root.right, x, y)

# Count number of students with scores less than a given score
def count_less(root, score):
    if root is None:
        return 0
    if root.score < score:
        return 1 + count_less(root.left, score) + count_less(root.right, score)
    else:
        return count_less(root.left, score)

# Menu-driven program
def main():
    root = None
    
    while True:
        print("\n===== Student Admission Ranking System =====")
        print("1. Insert Student")
        print("2. Print All Students (Sorted)")
        print("3. Search Student by Score")
        print("4. Print Students in Score Range")
        print("5. Print Rank of a Student")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            name = input("Enter student name: ")
            app_id = input("Enter application ID: ")
            score = int(input("Enter admission score: "))
            root = insert(root, name, app_id, score)

        elif choice == 2:
            print("\n--- Students in Ascending Order of Scores ---")
            inorder(root)

        elif choice == 3:
            score = int(input("Enter score to search: "))
            student = search(root, score)
            if student:
                print(f"Found: Name: {student.name}, ID: {student.application_id}, Score: {student.score}")
            else:
                print("Student not found!")

        elif choice == 4:
            x = int(input("Enter lower bound score: "))
            y = int(input("Enter upper bound score: "))
            print(f"\n--- Students with scores between {x} and {y} ---")
            print_range(root, x, y)

        elif choice == 5:
            score = int(input("Enter the score to find rank: "))
            rank = count_less(root, score)
            print(f"Number of students who scored less than {score}: {rank}")

        elif choice == 6:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
