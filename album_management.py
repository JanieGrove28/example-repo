# album_management.py

class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"

    # To improve printing of lists of Album objects
    def __repr__(self):
        return self.__str__()


def main():
    # Step 3: Create albums1 list with five Album objects
    albums1 = [
        Album("Abbey Road", 17, "The Beatles"),
        Album("Thriller", 9, "Michael Jackson"),
        Album("Back in Black", 10, "AC/DC"),
        Album("Rumours", 11, "Fleetwood Mac"),
        Album("Hotel California", 9, "Eagles"),
    ]
    print("Albums1 initial list:")
    print(albums1)

    # Step 4: Sort albums1 by number_of_songs
    albums1.sort(key=lambda album: album.number_of_songs)
    print("\nAlbums1 sorted by number_of_songs:")
    print(albums1)

    # Step 5: Swap element at position 1 (index 0) with element at position 2 (index 1)
    albums1[0], albums1[1] = albums1[1], albums1[0]
    print("\nAlbums1 after swapping first two elements:")
    print(albums1)

    # Step 6: Create albums2 list
    albums2 = []

    # Step 7: Add five Album objects to albums2 and print
    albums2.extend([
        Album("1989", 13, "Taylor Swift"),
        Album("The Wall", 26, "Pink Floyd"),
        Album("Led Zeppelin IV", 8, "Led Zeppelin"),
        Album("Nevermind", 12, "Nirvana"),
        Album("Goodbye Yellow Brick Road", 17, "Elton John"),
    ])
    print("\nAlbums2 initial list:")
    print(albums2)

    # Step 8: Copy all albums from albums1 into albums2
    albums2.extend(albums1)
    print("\nAlbums2 after copying albums1 into it:")
    print(albums2)

    # Step 9: Add two specific albums to albums2
    albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
    albums2.append(Album("Oops! . I Did It Again", 16, "Britney Spears"))
    print("\nAlbums2 after adding two more albums:")
    print(albums2)

    # Step 10: Sort albums2 alphabetically by album_name
    albums2.sort(key=lambda album: album.album_name.lower())
    print("\nAlbums2 sorted alphabetically by album_name:")
    print(albums2)

    # Step 11: Search for "Dark Side of the Moon" in albums2 and print its index
    index = next((i for i, album in enumerate(albums2) if album.album_name == "Dark Side of the Moon"), -1)
    if index != -1:
        print(f"\nIndex of 'Dark Side of the Moon' in albums2: {index}")
    else:
        print("\n'Dark Side of the Moon' not found in albums2")


if __name__ == "__main__":
    main()
# album_management.py

class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"

    # To improve printing of lists of Album objects
    def __repr__(self):
        return self.__str__()


def main():
    # Step 3: Create albums1 list with five Album objects
    albums1 = [
        Album("Abbey Road", 17, "The Beatles"),
        Album("Thriller", 9, "Michael Jackson"),
        Album("Back in Black", 10, "AC/DC"),
        Album("Rumours", 11, "Fleetwood Mac"),
        Album("Hotel California", 9, "Eagles"),
    ]
    print("Albums1 initial list:")
    print(albums1)

    # Step 4: Sort albums1 by number_of_songs
    albums1.sort(key=lambda album: album.number_of_songs)
    print("\nAlbums1 sorted by number_of_songs:")
    print(albums1)

    # Step 5: Swap element at position 1 (index 0) with element at position 2 (index 1)
    albums1[0], albums1[1] = albums1[1], albums1[0]
    print("\nAlbums1 after swapping first two elements:")
    print(albums1)

    # Step 6: Create albums2 list
    albums2 = []

    # Step 7: Add five Album objects to albums2 and print
    albums2.extend([
        Album("1989", 13, "Taylor Swift"),
        Album("The Wall", 26, "Pink Floyd"),
        Album("Led Zeppelin IV", 8, "Led Zeppelin"),
        Album("Nevermind", 12, "Nirvana"),
        Album("Goodbye Yellow Brick Road", 17, "Elton John"),
    ])
    print("\nAlbums2 initial list:")
    print(albums2)

    # Step 8: Copy all albums from albums1 into albums2
    albums2.extend(albums1)
    print("\nAlbums2 after copying albums1 into it:")
    print(albums2)

    # Step 9: Add two specific albums to albums2
    albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
    albums2.append(Album("Oops! . I Did It Again", 16, "Britney Spears"))
    print("\nAlbums2 after adding two more albums:")
    print(albums2)

    # Step 10: Sort albums2 alphabetically by album_name
    albums2.sort(key=lambda album: album.album_name.lower())
    print("\nAlbums2 sorted alphabetically by album_name:")
    print(albums2)

    # Step 11: Search for "Dark Side of the Moon" in albums2 and print its index
    index = next((i for i, album in enumerate(albums2) if album.album_name == "Dark Side of the Moon"), -1)
    if index != -1:
        print(f"\nIndex of 'Dark Side of the Moon' in albums2: {index}")
    else:
        print("\n'Dark Side of the Moon' not found in albums2")


if __name__ == "__main__":
    main()
