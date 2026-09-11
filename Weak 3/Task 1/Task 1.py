import json
import os

class Product:
    def __init__(self, product_id: str, name: str, price: float, quantity: int, category: str):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.category = category

    def to_dict(self):
        return self.__dict__


class Inventory:
    def __init__(self, filepath: str = "inventory.json"):
        self.filepath = filepath
        self.products = {}
        self.load_data()

    def add_product(self, product: Product):
        if product.product_id in self.products:
            print(f"❌ Error: Product ID '{product.product_id}' already exists.")
            return
        self.products[product.product_id] = product
        self.save_data()
        print(f"✅ Product '{product.name}' added successfully!")

    def delete_product(self, product_id: str):
        if product_id in self.products:
            del self.products[product_id]
            self.save_data()
            print(f"✅ Product ID '{product_id}' deleted successfully!")
        else:
            print(f"❌ Error: Product ID '{product_id}' not found.")

    def update_product(self, product_id: str, name: str = None, price: float = None, quantity: int = None, category: str = None):
        if product_id not in self.products:
            print(f"❌ Error: Product ID '{product_id}' not found.")
            return
        
        product = self.products[product_id]
        if name:
            product.name = name
        if price is not None:
            if price < 0:
                raise ValueError("Price cannot be negative.")
            product.price = float(price)
        if quantity is not None:
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            product.quantity = int(quantity)
        if category:
            product.category = category
            
        self.save_data()
        print(f"✅ Product ID '{product_id}' updated successfully!")

    def search_products(self, query: str):
        query = query.lower()
        results = [
            p for p in self.products.values()
            if query in p.name.lower() or query in p.product_id.lower() or query in p.category.lower()
        ]
        return results

    def display_table(self, product_list=None):
        if product_list is None:
            product_list = list(self.products.values())
            
        if not product_list:
            print("🔍 No products found.")
            return
        
        print("\n" + "-" * 78)
        print(f"{'ID':<8} | {'Product Name':<28} | {'Price':<10} | {'Qty':<6} | {'Category':<12}")
        print("-" * 78)
        for p in product_list:
            print(f"{p.product_id:<8} | {p.name:<28} | ${p.price:<9.2f} | {p.quantity:<6} | {p.category:<12}")
        print("-" * 78)

    def save_data(self):
        data = [p.to_dict() for p in self.products.values()]
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                try:
                    for item in json.load(f):
                        self.products[item["product_id"]] = Product(**item)
                except json.JSONDecodeError:
                    pass


def main():
    inv = Inventory()
    
    while True:
        print("\n==============================")
        print("     INVENTORY SYSTEM MENU    ")
        print("==============================")
        print("1. Add Product")
        print("2. Delete Product")
        print("3. Edit Product Details")
        print("4. Search Product")
        print("5. View All Products (Table)")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            print("\n--- Add New Product ---")
            try:
                pid = input("Product ID: ").strip()
                name = input("Product Name: ").strip()
                price = float(input("Price ($): "))
                qty = int(input("Quantity: "))
                cat = input("Category: ").strip()
                
                prod = Product(pid, name, price, qty, cat if cat else "General")
                inv.add_product(prod)
            except ValueError as e:
                print(f"❌ Invalid input: {e}")
                
        elif choice == "2":
            print("\n--- Delete Product ---")
            pid = input("Enter Product ID to delete: ").strip()
            inv.delete_product(pid)
            
        elif choice == "3":
            print("\n--- Edit Product Details ---")
            pid = input("Enter Product ID to update: ").strip()
            if pid in inv.products:
                p = inv.products[pid]
                print(f"Current -> Name: {p.name} | Price: ${p.price} | Qty: {p.quantity} | Category: {p.category}")
                print("Leave blank to keep existing value.")
                try:
                    new_name = input(f"New Name [{p.name}]: ").strip()
                    new_price_str = input(f"New Price [{p.price}]: ").strip()
                    new_qty_str = input(f"New Quantity [{p.quantity}]: ").strip()
                    new_cat = input(f"New Category [{p.category}]: ").strip()
                    
                    name = new_name if new_name else None
                    price = float(new_price_str) if new_price_str else None
                    qty = int(new_qty_str) if new_qty_str else None
                    cat = new_cat if new_cat else None
                    
                    inv.update_product(pid, name=name, price=price, quantity=qty, category=cat)
                except ValueError as e:
                    print(f"❌ Invalid input: {e}")
            else:
                print(f"❌ Error: Product ID '{pid}' not found.")
            
        elif choice == "4":
            print("\n--- Search Products ---")
            query = input("Enter keyword (Name, ID, or Category): ").strip()
            results = inv.search_products(query)
            inv.display_table(results)
                
        elif choice == "5":
            print("\n--- All Inventory Items ---")
            inv.display_table()
                
        elif choice == "6":
            print("\nExiting application. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()