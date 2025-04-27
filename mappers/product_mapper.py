import sqlite3
from domain.product import Product

class ProductMapper:
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection
        self._create_table()

    def _create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.connection.commit()

    def insert(self, product: Product):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO products (product_id, name, price) VALUES (?, ?, ?)
        ''', (product.product_id, product.name, product.price))
        self.connection.commit()

    def find(self, product_id: int) -> Product:
        cursor = self.connection.cursor()
        cursor.execute('SELECT product_id, name, price FROM products WHERE product_id = ?', (product_id,))
        row = cursor.fetchone()
        if row:
            return Product(*row)
        return None

    def list_all(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT product_id, name, price FROM products')
        rows = cursor.fetchall()
        return [Product(*row) for row in rows]
