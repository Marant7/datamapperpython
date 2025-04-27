import sqlite3
from domain.product import Product
from mappers.product_mapper import ProductMapper

def main():
    connection = sqlite3.connect(":memory:")  # In-memory database for testing
    mapper = ProductMapper(connection)

    # Inserting products
    mapper.insert(Product(1, "Laptop", 999.99))
    mapper.insert(Product(2, "Smartphone", 499.50))

    # Listing products
    products = mapper.list_all()
    for product in products:
        print(product)

    # Finding a product
    product = mapper.find(1)
    print(f"Found product: {product}")

if __name__ == "__main__":
    main()
