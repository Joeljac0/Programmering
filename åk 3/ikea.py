

class ikea:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
    
    def get_name(self):
        return self.name
    
    def set_name(self, value):
        self.name = value

    def get_category(self):
        return self.category
    
    def set_category(self, value):
        self.category = value

    def get_price(self):
        return self.price
    
    def set_price(self, value):
        self.price = value