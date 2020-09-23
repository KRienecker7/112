import os


def print_menu():
    print("--------------------------------------")
    print(" Kenny's Warehouse management system")
    print(" Welcome to a new way of inventory!")
    print("--------------------------------------")

    print('[1] Register new item')
    print('[2] Display Catalog')
    print('[3] Items out of stock')
    print('[4] Delete Item from Stock')
    print('[5] Update item stock')
    print('[6] Update item price')
    print('[7] Print Stock Value')
    print('[8] Print Categories')
    print('[x] Close')

def clear():
    return os.system('cls' if os.name == "nt" else 'clear') # one line is use because it targets just one thing but if there are other aspects then the if and else form is better spanning multiple lines

def print_header(title):
    clear()
    print("-" * 80)
    print(title)
    print("-" * 80)


def print_item(item):
    print(
        str(item.id).rjust(3)
        + " | " + item.title.ljust(25)
        + " | " + item.category.ljust(12)
        + " | " + str(item.stock).rjust(11)
        + " | $" + str (item.price).rjust(15)
    )


    """
    travel the catalog
    get the category of item
    asking, if the category does not exist in x array
        push the category into x array
        print the category
        
    """