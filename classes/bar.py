class Bar:
    def __init__(self, till, drinks):
        self.till = till
        self.drinks = drinks
    
    def add_new_drink(self, drink):
        self.drinks.append(drink)

    def check_underage(self, guest):
        return guest.age < 18

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink
        return

    def buy_drinks(self, drink_name, bar, guest):
        drink = self.find_drink_by_name(drink_name)
        if self.check_underage(guest) or guest.wallet < drink.price or guest.drunkeness > 10:
            guest.fun -= 1
            return 
        guest.increase_drunkeness(drink)
        guest.wallet -= drink.price
        guest.fun += 1