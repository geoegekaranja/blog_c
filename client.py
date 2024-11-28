import requests

API_URL = 'http://127.0.0.1:5000/products'

def add_product(name, description, price):
    response = requests.post(API_URL, json={'name': name, 'description': description, 'price': price})
    if response.status_code == 201:
        print(f"Product created: {response.json()}")
    else:
        print(f"Failed to create product: {response.status_code}, {response.json()}")

def get_products():
    response = requests.get(API_URL)
    if response.status_code == 200:
        print("Products list:")
        for product in response.json():
            print(product)
    else:
        print(f"Failed to retrieve products: {response.status_code}")

if __name__ == '__main__':
    # Add some products
    add_product("Laptop", "A high-performance laptop", 999.99)
    add_product("Smartphone", "A latest model smartphone", 499.99)

    # Get all products
    get_products()