class UndoRedo:
    def __init__(self):
        self.undo_stack=[]
        self.redo_stack=[]
    def Perform_action(self,action):
        self.undo_stack.append(action)
        self.redo_stack.clear()
    def Undo(self):
        if self.undo_stack is None:
            print("No action to undo.")
            return
        last_action=self.undo_stack.pop()
        self.redo_stack.append(last_action)
        print(f"Undo: {last_action} ")
    def Redo(self):
        if self.redo_stack is None:
            print("No action to Redo.")
            return
        last_action=self.redo_stack.pop()
        self.undo_stack.append(last_action)
        print(f"Redo: {last_action}")
editor = UndoRedo()
editor.Perform_action("Typed 'Hello'")
editor.Perform_action("Bolded 'Hello'")
editor.Perform_action("Added 'World'")
print()
editor.Undo()
editor.Undo()
print()
editor.Redo()
editor.Redo()
print(editor.undo_stack)
print(editor.redo_stack)

        