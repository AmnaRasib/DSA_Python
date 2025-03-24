# Task 3: Music Playlist System using a Doubly Linked List
class Song:
    def __init__(self,title):
        self.title=title
        self.next=None
        self.prev=None
class MusicPlaylist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.current_song=None
    def add_song(self,title):
        song=Song(title)
        if self.head is None:
            self.head=song
            self.tail=song
            self.current_song=song
        else:
            self.tail.next=song
            song.prev=self.tail
            self.tail=song
    def play_next(self):
        if self.current_song and self.current_song.next:
            self.current_song=self.current_song.next
            print(f"Now Playing: {self.current_song.title}")
        else:
            print("End of playlist reached!")
    def play_previous(self):
        if self.current_song and self.current_song.prev:
            self.current_song=self.current_song.prev
            print(f"Now Playing: {self.current_song.title}")
        else:
            print("Already at the first song!")
    def display_playlist(self):
        current=self.head
        while current:
            print(current.title,"<->",end=" ")
            current=current.next
        print("None")

playlist=MusicPlaylist()
playlist.add_song("Song 1")
playlist.add_song("Song 2")
playlist.add_song("Song 3")
playlist.add_song("Song 4")
playlist.add_song("Song 5")

print("\nMusic Playlist: ")
playlist.display_playlist()

print("\nNavigating Playlist: ")
playlist.play_next()
playlist.play_next()
playlist.play_next()
playlist.play_previous()
playlist.play_previous()
