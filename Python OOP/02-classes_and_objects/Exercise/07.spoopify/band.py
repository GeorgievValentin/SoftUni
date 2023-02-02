import argparse

import pyexpat

from oop.oop_exams.retake_exam_22_august_2022.project import Album
from oop.oop_exams.retake_exam_22_august_2022.project import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for album in self.albums:
            if album.published:
                return f"Album has been published. It cannot be removed."

        try:
            album = next(filter(lambda a: a.name == album_name, self.albums))
        except StopIteration:
            return f"Album {album_name} is not found."

        self.albums.remove(album)
        return f"Album {album.name} has been removed."

    def details(self):
        result = [f"Band {self.name}"]
        [result.append(f"{a.details()}") for a in self.albums]

        return "\n".join(result)


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
