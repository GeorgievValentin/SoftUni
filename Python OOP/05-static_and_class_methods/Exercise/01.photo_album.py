from math import ceil


class PhotoAlbum:
    PHOTOS_ON_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages  # count of pages in the album
        self.photos = [[] for _ in range(pages)]  # makes pages as empty lists each

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / PhotoAlbum.PHOTOS_ON_PAGE))

    def add_photo(self, label: str):
        for page in range(self.pages):                              # for each page in the album (range of pages)
            if len(self.photos[page]) < PhotoAlbum.PHOTOS_ON_PAGE:  # check if reach the limit of a page
                self.photos[page].append(label)                     # add photo with name to the current page
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"

        return "No more free slots"

    def display(self):
        result = ["-" * 11]

        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append("-" * 11)

        return "\n".join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
