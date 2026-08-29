
inventory = {'aa': {'price': 15, 'quantity': 11},'bb': {'price': 15, 'quantity': 0}}
def entry_point():



    while True:
        print("""=========== Inventory Manager ===========
1. Add Product
2. View Products
3. Search Product
4. Update Quantity
5. Delete Product
6. Show Available Products
7. Show Out of Stock Products
8. Exit""")


        user_input = get_valid_choice()

        
        if user_input == 1:
            print("======= Add product =======")
            add_product(inventory)

        elif user_input == 2:
            print("======= products =======")
            view_products(inventory)
        elif user_input == 3:
            print("======= Search Products =======")
            search_product(inventory)
        elif user_input == 4:
            print("======= Update Product =======")
            update_product(inventory)
        elif user_input == 5:
            print("======= Delete Product =======")
            delete_product(inventory)
        elif user_input == 6:
            print("=======  Avaliable Products =======")
            avaliable_products(inventory)
        elif user_input == 7:
            print("======= Out Of Stock Products =======")
            out_of_stock(inventory)
        elif user_input == 8:
            print("======= Exit =======")
            print("Goodbye 👋")
            break
        else:
            print("Please enter valid input")
            continue

def get_valid_choice():
    while True:
        try:
            return int(input("Choose an option: "))
        except ValueError:
            print("Please enter valid number.")


def get_valid(message):
     while True:
        try:
            value = int(input(message))

            if value < 0:
                print("Please enter a number greater than or equal to 0.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")



def add_product(inventory):
    while True:
        product_name = input("Add product name: ").strip().lower()

        if len(product_name) == 0:
            print("Please add a valid name")
            continue

        if product_name in inventory:
            print("Product already exists!")
            print(f"Product: {product_name}")
            print(f"Price: {inventory[product_name]["price"]}")
            print(f"Quantity: { inventory[product_name]["quantity"]}")

            new_price = get_valid("Add product price: ")
            new_quantity = get_valid("Add product quantity: ")

            if new_price == inventory[product_name]["price"]:
                inventory[product_name]["quantity"] += new_quantity
                print("Quantity updated successfully.")
                return

            elif new_price != inventory[product_name]["price"]:
                check_input = input(
                    "You will update price of product (y|n): "
                ).strip().lower()

                if check_input == "y":
                    inventory[product_name]["price"] = new_price
                    inventory[product_name]["quantity"] += new_quantity
                    print("Price and quantity updated successfully.")
                    return

                elif check_input == "n":
                    inventory[product_name]["quantity"] += new_quantity
                    print("Price kept. Quantity updated successfully.")
                    return

                else:
                    print("Please enter y or n.")
                    continue

        product_price = get_valid("Add product price: ")
        product_quantity = get_valid("Add product quantity: ")

        inventory[product_name] = {
            "price": product_price,
            "quantity": product_quantity
        }

        print("Product added successfully.")
        return

def view_products(inventory):
    if not inventory:
        print("There are no products.")
        return

    for key, value in inventory.items():
        print(f"Name: {key}")
        print(f"Price: {value['price']}")
        print(f"Quantity: {value['quantity']}")
        print("--------------------")

def search_product(inventory):
    name = input("Enter product name: ").lower().strip()

    if name in inventory:
        print("✅ Product Found")

        print(f"Name: {name}")
        print(f"Price {inventory[name]["price"]}")
        print(f"Quantity {inventory[name]["quantity"]}")

        return

    print("❌ Product not found.")

def update_product(inventory):
    name = input("Enter product name: ").lower().strip()

    if name in inventory:
        print("✅ Product Found")
        print(f"Name: {name}")
        print(f"Price {inventory[name]["price"]}")
        print(f"Price {inventory[name]["quantity"]}")
        print("--------------------")


        while True:
            user_input = get_valid("""
1- update Price
2 update Quantity
enter your choice: """)

            if user_input == 1:
                new_price = get_valid("Enter new Price: ")
                inventory[name]["price"] = new_price

                print("✅ Price updated successfully.")
                return
            elif user_input == 2:
                new_quan = get_valid("Enter new Quantity: ")
                inventory[name]["quantity"] = new_quan

                print("✅ Quantity updated successfully.")
                return
        

            print("Please Enter valid input")
            continue

def delete_product(inventory):
    while True:
        name = input("Enter product name: ").lower().strip()
    
        if name in inventory:
            print("✅ Product Found")
            print(f"Name: {name}")
            print(f"Price {inventory[name]["price"]}")
            print(f"Quantity {inventory[name]["quantity"]}")
            print("--------------------")

            while True:
                check_input = input("Are you sure? y/n: ").lower()

                if check_input == "y":
                    del inventory[name]
                    print("✅ Product deleted.")
                    return

                elif check_input == "n":
                    print("❌ Delete cancelled.")
                    return

                else:
                    print("Please enter y or n.")
                    continue
    
        print("The product not found")
        continue
    

def avaliable_products(inventory):
    found = False

    for key, value in inventory.items():
        if value["quantity"] > 0:
            print(f"{key} ---> {value['quantity']}")
            found = True

    if not found:
        print("Not found")

def out_of_stock(inventory):
    found = False

    for key,value in inventory.items():
        if value["quantity"] == 0:
            print(f"{key}")
            found = True

    if not found:
        print("Not found")

entry_point()