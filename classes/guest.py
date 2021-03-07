class Guest:

    def __init__(self, name, age, wallet, fun, drunkeness, favourite_artist, 
                favourite_song, room_number, checked_in):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.fun = fun
        self.drunkeness = 0
        self.favourite_artist = favourite_artist
        self.favourite_song = favourite_song
        self.room_number = None
        self.checked_in = False

    def find_favourite_song(self, room, song):
        for song in room.songs:
            if song.title == self.favourite_song:
                self.fun += 2
                if self.fun > 10:
                    self.rowdiness = 10
                return 'Wooo! This is my favourite song!'
        return

    def find_favourite_artist(self, room, song):
        for song in room.songs:
            if song.artist == self.favourite_artist:
                self.fun += 1
                if self.fun > 10:
                    self.fun = 10
                return 'Nice, I love this band!'
        return

    def increase_drunkeness(self, drink):
        self.drunkeness += drink.alcohol_level