# Simulate a Git commit history where commits are stored in a linked list.
import datetime
class CommitNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.timestamp=datetime.datetime.now()
class GitHistory:
    def __init__(self):
        self.head=None
        self.tail=None
    def commit(self,message):
        node=CommitNode(message)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def show_history(self):
        current=self.head
        if current is None:
            print("No commit in history.")
            return
        print("Commint History: ")
        while current:
            print(f"Commit: {current.data}, Date: {current.timestamp}")
            current=current.next
    def undo_commit(self):
        if self.head is None:
            print("No commit to undo")
            return
        self.tail=self.tail.next
        print("Last Commit undone")

git=GitHistory()
git.commit("Intial commit")
git.commit("Added README file")
git.commit("Implemented New Python Features")
git.show_history()
git.undo_commit()
git.show_history()
