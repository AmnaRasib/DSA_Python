class Node:
    def __init__(self, content):
        self.content = content
        self.next = None

class TextEditor:
    def __init__(self):
        self.head = None  # Points to the most recent state
        self.current = None  # Points to the current state

    def append(self, text):
        # Create a new node for the current text
        new_node = Node(text)
        if self.head is None:
            self.head = new_node  # First node
            self.current = new_node  # Current state is the first node
        else:
            # Insert the new node at the head (most recent state)
            new_node.next = self.head
            self.head = new_node
            self.current = new_node  # Update current to the new head

    def display(self):
        if self.current is None:
            print("Current content: ''")
        else:
            print(f"Current content: '{self.current.content}'")

    def undo(self):
        if self.head is None:
            print("Nothing to undo")
            return
        
        # Move to the next node (previous state)
        if self.head.next is None:
            # If there's only one node, clear the current
            self.current = None
        else:
            # Move to the next node
            self.current = self.head.next
        
        # Update head to the current state
        self.head = self.current

# Example usage
if __name__ == "__main__":
    editor = TextEditor()

    # Typing text
    editor.append("Hello")
    editor.display()  # Output: Current content: 'Hello'

    editor.append(" World")
    editor.display()  # Output: Current content: ' World'

    # Undo last action (removing " World")
    editor.undo()
    editor.display()  # Output: Current content: 'Hello'
    
    # Undo again (removing "Hello")
    editor.undo()
    editor.display()  # Output: Current content: ''