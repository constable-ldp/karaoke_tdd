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

        #if time == 0: check_out(0)

    