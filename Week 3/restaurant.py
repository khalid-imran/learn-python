from abc import ABC

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.items = []

    def show_menu(self):
        print("\n")
        print("--- Item Lists ---")
        for item in self.items:
             print(f"ID: {item.id} Name: {item.name} Price: {item.price} Quantity: {item.quantity}\n")

class Item():
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class Users(ABC):
    
    def __init__(self,id,name,email,address):
        self.id = id
        self.name = name
        self.email = email
        self.address = address


class Customer(Users):
    def __init__(self, id, name, email, address):
        super().__init__(id, name, email, address)
        self.wallet = 0
        self.orders = []
        
    def add_order(self):
        if self.wallet == 0:
            print(f"Your balance is empty. Please add money first")
        else:
            item_id = int(input("Enter Item Id for order : "))
            for item in restaurant.items:
                    if item.id == item_id:
                        self.orders.append(item)
                        self.wallet -= item.price
                        item.quantity = item.quantity-1
                        print(f"{item.id} id item order Successfully!")
                        print(f"Your current balance is {self.wallet}")
                            

    def list_of_orders(self):
        print("\n")
        print("--- Order List ---")
        for item in self.orders:
            print(f"ID: {item.id} Name: {item.name} Price: {item.price} Quantity: {item.quantity}\n")
    
    def add_money(self):
        amount = float(input("Enter Amount: "))
        self.wallet += amount
        print(f"{amount} added to your wallet")
    
    def check_balance(self):
        print(f"Your balance is {self.wallet}")


class Admin(Users):
    
    def __init__(self, id, name, email, address, restaurant):
        super().__init__(id, name, email, address)
        self.customers = restaurant.customers
        self.items = restaurant.items
   
    def add_customer(self):
        id = int(input("Enter Customer id : "))
        name = input("Enter Customer name : ")
        email = input("Enter Customer email : ")
        address = input("Enter Customer address : ")
        customer = Customer(id, name ,email ,address)
        self.customers.append(customer)
        print(f"Customer {customer.name} added successfully")
    
    def remove_customer(self):
        id = int(input("Enter id of Customer: "))
        for customer in self.customers:
            if customer.id == id:
                self.customers.remove(customer)
                print(f"Customer {customer.name} removed Successfully!")
    
    def view_customers(self):
        print("\n")
        print("--- Customers List ---")
        for customer in self.customers:
            print(f"ID: {customer.id} Name: {customer.name} Email: {customer.email} Address: {customer.address}\n")

    def add_item(self):
        id = int(input("Enter item id : "))
        name = input("Enter item name : ")
        price = float(input("Enter item price : "))
        quantity = int(input("Enter item quantity : "))
        item = Item(id, name, price, quantity)
        self.items.append(item)
        print(f"{item.name} added successfully.")
    
    def remove_item(self):
        item_id = int(input("Enter id of item : "))
        for item in self.items:
            if item.id == item_id:
                self.items.remove(item)
                print(f"{item.name} removed successfully.")
    
    def update_item_price(self):
        item_id = int(input("Enter item id : "))
        value = float(input("Enter item price : "))
        for item in self.items:
            if item.id == item_id:
                item.price = value
                print(f"Updated {item.name} with price {item.price} successfully.")

    def view_menu(self):
       restaurant.show_menu()
            
restaurant = Restaurant("Chillox")

admin = Admin(1, "Admin", "admin@gmail.com", "Dhaka", restaurant)

while(True):
    print("restaurant Management System!")
    print("1. Admin Login")
    print("2. Customer Login")
    print("3. Exit")
    
    main_option = int(input("Enter your Option: "))
    
    if main_option == 1:
        admin_name = input("Enter Admin Name: ")
        if admin.name == admin_name:
            while(True):
                print('\n')
                print(f"Welcome {admin.name}")
                print("--- Admin Menu ---")
                print("1. Create Customer")
                print("2. Remove Customer")
                print("3. View all Customers")
                print("4. Manage restaurant Menu")
                print("5. Exit")
            
                option = int(input("Enter Option: "))
                
                if option == 1:
                    admin.add_customer()
                elif option == 2:
                    admin.remove_customer()
                elif option == 3:
                    admin.view_customers()
                elif option == 4:
                    while(True):
                        print("\n")
                        print("--- Manage restaurant Menu ---")
                        print("1. View Customers")
                        print("2. Add Item")
                        print("3. Remove Item")
                        print("4. Update Items using Price")
                        print("5. View Items")
                        print("6. Exit")
                        
                        res_option = int(input("Enter your Option: "))
                        
                        if res_option == 1:
                            admin.view_customers()
                        elif res_option == 2:
                            admin.add_item()
                        elif res_option == 3:
                            admin.remove_item()
                        elif res_option == 4:
                            admin.update_item_price()
                        elif res_option == 5:
                            admin.view_menu()
                        elif res_option == 6:
                            break
                        else:
                            print("Invalid Option!")
                            
                elif option == 5:
                    break
                else:
                    print("Invalid Option!")
        else:
            print("Admin name does not !")
         
    elif main_option == 2:
        customer_name = input("Enter your name: ")
        for customer in restaurant.customers:
            if customer.name == customer_name:
                while(True):
                    print(f"--- {customer.name}'s Menu ---")
                    print("1. View restaurant menu")
                    print("2. View Balance")
                    print("3. Add Balance")
                    print("4. Place Order")
                    print("5. View Past Orders")
                    print("6. Exit")
                    
                    customer_option = int(input("Enter Option: "))
                    
                    if customer_option == 1:
                        restaurant.show_menu()
                        
                    elif customer_option == 2:
                        customer.check_balance()
                        
                    elif customer_option == 3:
                        customer.add_money()
                        
                    elif customer_option == 4:
                        customer.add_order()
                        
                    elif customer_option == 5:
                        customer.list_of_orders()
                        
                    elif customer_option == 6:
                        break
                    else:
                        print("Invalid Option!")
    elif main_option == 3:
        break
    else:
        print("Invalid Option!")