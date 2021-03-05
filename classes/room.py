class Room:
    def __init__(self, room_number, price, current_capacity, max_capacity, premium):
        self.room_number = room_number
        self.price = price
        self.current_capacity = current_capacity
        self.max_capacity = max_capacity
        self.premium = premium

    def check_in(self, guest):
        if guest.checked_in == True 
        or self.current_capacity == self.max_capacity 
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
        guest.checked_in == False

    def add_song(self):

        

        #guest pays price
        
        #room number capacity increases


