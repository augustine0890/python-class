from datetime import time


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def calculate_bill(self, purchased_items):
        price = 0
        for item in purchased_items:
            price += self.items[item]
        return price

    def __repr__(self):
        return "Menu {name} available from {start} to {end}".format(name=self.name, start=self.start_time, end=self.end_time)


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    
    def available_menus(self, time):
        menu_list = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                menu_list.append(menu.name)
        return menu_list

    def __repr__(self):
        return "Address: {}".format(self.address)


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchines = franchises

    def __repr__(self):
        return "{name} in {place}".format(name=self.name, place=self.franchines[0].address)


brunch = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, time(hour=11), time(hour=16))
early_bird = Menu("early_bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, time(hour=15), time(hour=18))
dinner = Menu("dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, time(hour=17), time(hour=23))
kids = Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, time(hour=11), time(hour=21))

print(kids)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
print(new_installment)
print(new_installment.available_menus(time(hour=12)))
print(new_installment.available_menus(time(hour=17)))

arepas_menu = Menu("arepas_menu", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, time(hour=10), time(hour=20))
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
arepas = Business("Take a' Arepa", [arepas_place])
print(arepas)