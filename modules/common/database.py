import sqlite3

class Database():
    def __init__(self):
        self.connection = sqlite3.connect(r'/Users/gs/GS_QA_auto'+r"/become_qa_auto.db")
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f'Connected successfully. SQLite Database version is: {record}')

    def get_all_users(self):
        querry = 'SELECT ID, name, address, city FROM customers'
        self.cursor.execute(querry)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        querry = f"SELECT name, address, city FROM customers WHERE name = '{name}'"
        self.cursor.execute(querry)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        querry = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(querry)
        self.connection.commit()

    def get_prodcut_qnt_by_id(self, product_id):
        querry = f"SELECT name, quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(querry)
        product = self.cursor.fetchall()
        return product
    
    def insert_product(self, id, name, descr, qnt):
        querry = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({id}, '{name}', '{descr}', {qnt})"
        self.cursor.execute(querry)
        self.connection.commit()

    def delete_product(self, product_id):
        querry = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(querry)
        self.connection.commit()

    def get_detailed_orders(self):
        querry = "SELECT orders.id, customers.name, products.name, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(querry)
        record = self.cursor.fetchall()
        return record 
    
    def add_order(self, order_id, customer_id, product_id, order_date=None):
        querry = f"INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date) \
            VALUES ({order_id}, {customer_id}, {product_id}, '{order_date}')"
        self.cursor.execute(querry)
        self.connection.commit()
