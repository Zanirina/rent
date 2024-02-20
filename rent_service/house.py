from rent_service.buildings import Building


class House(Building):
    def __init__(self, address, id, category, price, num_bedrooms, square_footage):
        super().__init__(address, id, category, price, num_bedrooms, square_footage)
        self.address = address
        self.id = id
        self.category = category
        self.price = price
        self.num_bedrooms = num_bedrooms
        self.square_footage = square_footage
    def toString(self):
        print(str(f"Address: {self.address}\nID: {self.id}\nCategory: {self.category}"
                  f"\nPrice: {self.price}\nNumber of bedrooms: {self.num_bedrooms}\nArea: {self.square_footage}"))
        print("---------------------------------------")

