class Room:
    
    def __init__(self, room_number, price, songs, current_capacity, max_capacity):
        self.room_number = room_number
        self.price = price
        self.current_capacity = current_capacity
        self.songs = songs
        self.max_capacity = max_capacity

    def check_in(self, guest):
        if guest.checked_in == True \
        or self.current_capacity == self.max_capacity \
        or guest.wallet < self.price:
            return
        guest.room_number = self.room_number
        guest.wallet -= self.price
        self.current_capacity += 1
        guest.checked_in = True

    def check_out(self, guest):
        if guest.checked_in == False:
            return
        self.current_capacity -= 1
        guest.checked_in = False

    def add_song(self, song):
        for current_song in self.songs:
            if current_song == song:
                return
        self.songs.append(song)