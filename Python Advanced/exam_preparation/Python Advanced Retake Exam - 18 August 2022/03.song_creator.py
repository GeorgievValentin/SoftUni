from os import linesep


def add_songs(*args):

    songs = {}
    result = []
    for data in args:
        name = data[0]
        lyrics = data[1]
        if name not in songs:
            songs[name] = lyrics
        else:
            songs[name].extend(lyrics)
    for key, value in songs.items():
        result.append("- " + key)
        if value:
            result.extend(value)
    return linesep.join(result)


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))

print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who'value wrong or right"]),
))
