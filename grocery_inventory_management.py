
class GroceryStore:
    def __init__(self):
     self.inventory={}

    def  add_product(self,product,quantity):
        if product in self.inventory:
            self.inventory[product]+=quantity
        else:
            self.inventory[product]=quantity

    def update_product(self,product,new_quantity):
        if product in self.inventory:
            self.inventory[product]=new_quantity
            print(f"Update {product} quantity   to :{new_quantity}.")
        else:
            print(f"{product}not found in inventory.")

    def remove_product(self,product):
        if product in self.inventory:
            del self.inventory[product]
            print(f"Removed{product}from inventory.")
        else:
            print(f"{product}not found in inventory.")

    def display_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for product ,quantity in self.inventory.items():
                print(f"{product}: {quantity}")
store = GroceryStore()
store.add_product("Apple",50)
store.add_product("Banana",40)
store.add_product("Guva",20)
store.add_product("Pomegranate",100)
store.display_inventory()
store.update_product("Pomegranate",150)
store.display_inventory()
store.remove_product("Guva")
store.display_inventory()

