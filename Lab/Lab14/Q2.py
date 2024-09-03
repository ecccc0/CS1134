from ChainingHashTableMap import *
from DoublyLinkedList import *

class PlayList:
    def __init__(self):
        self.sequence = DoublyLinkedList()
        self.map = ChainingHashTableMap()

    def add_song(self, new_song_name):
        self.map[new_song_name] = self.sequence.add_last(new_song_name)

    def add_song_after(self, song_name, new_song_name):
        if song_name not in self.map:
            raise Exception("song is not in playlist")
        self.sequence.add_after(self.map[song_name], new_song_name)

    def play_song(self, song_name):
        if song_name not in self.map:
            raise Exception("song is not in playist")
        print("Playing " + song_name)

    def play_list(self):
        cursor = self.sequence.header.next
        while cursor is not self.sequence.trailer:
            print("Playing " + cursor.data)
            cursor = cursor.next
    