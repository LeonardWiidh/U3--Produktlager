import csv
import os
import locale

products = []

def load_data(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )

def save_data(filename):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['id', 'name', 'desc', 'price', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for product in products:
            writer.writerow(product)

def get_product(products, id):
    for product in products:
        if product['id'] == id:
            return product
    return None

def get_products(products):
    product_list = []
    for product in products:
        product_info = f"{product['id']} \t {product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)} \t {product['quantity']}"
        product_list.append(product_info)
    
    return "\n".join(product_list)

def add_product():
    id = int(input("ID: "))
    name = input("Name: ")
    desc = input("Description: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    
    products.append(
        {
            "id": id,
            "name": name,
            "desc": desc,
            "price": price,
            "quantity": quantity
        }
    )
    print("produkten ha lags till")
    save_data('db_products.csv')

def remove_product():
    id = int(input("id av produkten som du vill ta bort: "))
    product = get_product(products, id)
    if product:
        products.remove(product)
        print("Produkten har tagits bort")
        save_data('db_products.csv')
    else:
        print("Produkten hittades inte.")

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

os.system('cls')
load_data('db_products.csv')

while True:
    print("""\nprodukter
    1. visa produkter
    2. lägg till en pordukt
    3. ta bort en produkt
    4. Quit""")
    
    choice = input("välj ett alternativ: ")
    
    if choice == '1':
        print(get_products(products))
    elif choice == '2':
        add_product()
    elif choice == '3':
        remove_product()
    elif choice == '4':
        break
    else:
        print("error försök igen.")
