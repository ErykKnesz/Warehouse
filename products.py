
class Product:
    def __init__(self, name, unit, unit_price, quantity):
        self.name = name
        self.unit = unit
        self.unit_price = unit_price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} {self.unit} {self.unit_price} {self.quantity}"

    def add_item(item):
        item.pop('csrf_token')
        ITEMS[item] = item 
        return 

    def sell_item(item):
        item.pop('csrf_token')
        if ITEMS[item.name] == item:
            pass
        return  


item_1 = Product(name='apple juice', unit='l', unit_price=1.99, quantity=45.03)
item_2 = Product(name='cake flour', unit='kg', unit_price= 1.23, quantity=644.09)
ITEMS = {
    item_1.name: item_1,
    item_2.name: item_2,
}



