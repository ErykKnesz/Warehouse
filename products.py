from decimal import *
import csv


class Product:
    def __init__(self, name, unit, unit_price, quantity):
        self.name = name
        self.unit = unit
        self.unit_price = Decimal(unit_price)
        self.quantity = Decimal(quantity)

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
            new_quantity = item['quantity'] + ITEMS[item['name']].quantity
            ITEMS[item['name']] = Product(name=item['name'], unit=item['unit'],
                                           unit_price=item['unit_price'],
                                           quantity=new_quantity)
        return

    def sell_item(form, product_to_sell):
        if product_to_sell in ITEMS.keys():
            product_to_sell = ITEMS.get(product_to_sell)
            new_quantity = product_to_sell.quantity - form['quantity']
            if new_quantity < 0:
                new_quantity = 0
            product_to_sell.quantity = new_quantity
        return new_quantity

    def save_csv(ITEMS):
        with open("warehouse.csv", "w", newline='') as f:
            field_names = ['name', 'unit', 'unit_price', 'quantity']
            products = [product for product in ITEMS.values()]
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writeheader()
            for product in products:
                writer.writerow({'name': product.name, 'unit': product.unit, 'unit_price': product.unit_price, 'quantity': product.quantity})

    def import_csv():
        with open("warehouse.csv", "r", newline='') as f:
            ITEMS.clear()
            reader = csv.DictReader(f)
            for row in reader:
                ITEMS[row['name']] = Product(name=row['name'], unit=row['unit'], unit_price=row['unit_price'], quantity=row['quantity'])
        return ITEMS


item_1 = Product(name='apple juice', unit='l', unit_price=1.99, quantity=45.03)
item_2 = Product(name='cake flour', unit='kg', unit_price=1.23, quantity=644.09)
ITEMS = {
    item_1.name: item_1,
    item_2.name: item_2,
}