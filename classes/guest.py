class Guest:

    def __init__(self, name, age, wallet, rowdiness, drunkeness, prefers_premium,
                 favourite_artist, favourite_song, room_number, checked_in, time):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.rowdiness = rowdiness
        self.drunkeness = 0
        self.prefers_premium = prefers_premium
        self.favourite_artist = favourite_artist
        self.favourite_song = favourite_song
        self.room_number = None
        self.checked_in = False
        self.time = time

    def find_favourite_song(self, room, song):
        for song in room.songs:
            if song.title == self.favourite_song:
                self.rowdiness += 2
                if self.rowdiness > 10:
                    self.rowdiness = 10
                return 'Wooo! This is my favourite song!'
        return

    def find_favourite_artist(self, room, song):
        for song in room.songs:
            if song.artist == self.favourite_artist:
                self.rowdiness += 1
                if self.rowdiness > 10:
                    self.rowdiness = 10
                return 'Nice, I love this band!'
        return

    def increase_drunkeness(self, drink):
        self.drunkeness += drink.alcohol_level