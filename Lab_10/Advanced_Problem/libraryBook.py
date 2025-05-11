class BookNode:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.left = None
        self.right = None

def insert(root, title, isbn):
    if root is None:
        return BookNode(title, isbn)
    if title < root.title:
        root.left = insert(root.left, title, isbn)
    elif title > root.title:
        root.right = insert(root.right, title, isbn)
    return root  

def search(root, title):
    if root is None:
        return None
    if title == root.title:
        return root
    elif title < root.title:
        return search(root.left, title)
    else:
        return search(root.right, title)

def min_value(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete_book(root, title):
    if root is None:
        return root
    if title < root.title:
        root.left = delete_book(root.left, title)
    elif title > root.title:
        root.right = delete_book(root.right, title)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Node with two children
        temp = min_value(root.right)
        root.title = temp.title
        root.isbn = temp.isbn
        root.right = delete_book(root.right, temp.title)
    return root

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(f"{node.title} (ISBN: {node.isbn})")
        inorder_traversal(node.right)
# Create the tree and add books
root = None
root = insert(root, "Harry Potter", "9780747532743")
root = insert(root, "The Hobbit", "9780547928227")
root = insert(root, "Pride and Prejudice", "9781503290563")
root = insert(root, "1984", "9780451524935")

print("Books in Alphabetical Order:")
inorder_traversal(root)

print("\nDeleting 'The Hobbit'...")
root = delete_book(root, "The Hobbit")

print("\nBooks after Deletion:")
inorder_traversal(root)

