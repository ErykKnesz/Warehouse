import csv
import sys
import tabulate

items = [
    {
    'name': 'Coca-Cola', 
    'quantity': 20,
    'unit': 'bottle', 
    'unit_price': 2.32
    },
    {
    'name': 'water',
    'quantity': 50,
    'unit': 'bottle',
    'unit_price': 1.15
    },
    {
    'name': 'beer',
    'quantity': 10,
    'unit': 'barrel',
    'unit_price': 15
    }
    ]

sold_items = []


def get_items():
    headings = items[0].keys()
    rows = [a_dict.values() for a_dict in items]
    print(tabulate.tabulate(rows, headings))

    return None


def add_item():
    dictionary = {
        'name': input("Please provide product name: "),
        'quantity': float(input("Please provide product quantity: ")),
        'unit': input("Please provide unit name: "),
        'unit_price': float(input("Please provide unit price: "))
        }
    return dictionary


def sell_item(name_to_sell, quantity_to_sell):
    for dictionary in items:
        stock_name = dictionary.get('name')
        if name_to_sell == stock_name.lower():
            stock_quantity = dictionary.get('quantity')
            dictionary['quantity'] = stock_quantity - quantity_to_sell
            sold_items.append(
                {
                    'name': name_to_sell,
                    'quantity': quantity_to_sell,
                    'unit': dictionary['unit'],
                    'unit_price': dictionary['unit_price']
                }
                )


def get_costs():
    costs = [
        a_dict.get('quantity') * a_dict.get('unit_price')
        for a_dict in items
        ]
    return sum(costs)


def get_income():
    revenue = [
        a_dict.get('quantity') * a_dict.get('unit_price')
        for a_dict in sold_items
        ]
    return sum(revenue)


def get_profit():
    costs = get_costs()
    revenue = get_income()
    profit = revenue - costs
    return round(profit, 2)


def export_items_to_csv():
    field_names = ['name', 'quantity', 'unit', 'unit_price']
    with open('warehouse.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(items)


def export_sales_to_csv():
    field_names = ['name', 'quantity', 'unit', 'unit_price']
    with open('sold_items.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(sold_items)


def load_items_from_csv(path):
    items.clear()
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append(row)
    for a_dict in items:
        for key, value in a_dict.items():
            try:  
                a_dict[key] = float(value)
            except ValueError:
                a_dict[key] = str(value)


def menu():
    # prompts user to state desired action and proceeds accordingly
    user = input("What would you like to do? ").lower()
    if user == 'exit':
        print("Exitting...bye!") 
        exit()
    if user == 'show':
        get_items()
    if user == 'add':
        items.append(add_item())
        print("Congrats! New item added. See the new stock-status")
        get_items()
    if user == 'sell':
        name_to_sell = input("Which product to sell?").lower()
        quantity_to_sell = float(input("How much to sell?"))
        sell_item(name_to_sell, quantity_to_sell)
        print("Sell action completed! See the new stock-status!")
        get_items()
        print(f"Here's what you sold already! \n {sold_items}")
    if user == 'show cost':
        print(f"your total cost equal: {get_costs()}")
    if user == 'show revenue':
        print(f"your total revenue equals: {get_income()}")
    if user == 'show profit':
        print(f"your net result equals: {get_profit()}")
    if user == 'save':
        print("Succesfully exported data to .csv extension")
        export_items_to_csv()
        export_sales_to_csv()
    if user == 'load':
        print("Succesfully loaded data from .csv extension")
        load_items_from_csv('warehouse.csv')
        print("See updated stock status")
        get_items()


if __name__ == "__main__":
    if len(sys.argv[:]) > 1:
        path = sys.argv[1]
        load_items_from_csv(path)
    while True:
        menu()
