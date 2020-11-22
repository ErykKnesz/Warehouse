from decimal import *


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
        if item['name'] not in ITEMS.keys():
            new_product = Product(name=item['name'], unit=item['unit'],
                                  unit_price=item['unit_price'],
                                  quantity=item['quantity'])
            ITEMS[new_product.name] = new_product
        else:
             ITEMS[item['name']] = Product(name=item['name'], unit=item['unit'],
                                           unit_price=item['unit_price'],
                                           quantity=item['quantity'])
        return 

    def sell_item(form, product_to_sell):
        form.pop('csrf_token')
        if product_to_sell in ITEMS.keys():
            product_to_sell = ITEMS.get(product_to_sell)
            new_quantity = Decimal(product_to_sell.quantity) - form['quantity']
            product_to_sell.quantity = new_quantity
        return new_quantity


item_1 = Product(name='apple juice', unit='l', unit_price=1.99, quantity=45.03)
item_2 = Product(name='cake flour', unit='kg', unit_price=1.23, quantity=644.09)
ITEMS = {
    item_1.name: item_1,
    item_2.name: item_2,
}