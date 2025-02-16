# Store a list of songs and provide a method to display them.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class PlaylistManager:
    def __init__(self):
        self.head=None
        self.tail=None
    def append_Song(self,song):
        node=Node(song)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def display_MusicList(self):
        current=self.head
        while current:
            print(current.data,end=" -> ")
            current=current.next
        print ("None")
m=PlaylistManager()
m.append_Song("abc")
m.append_Song("xyz")
m.display_MusicList()

        