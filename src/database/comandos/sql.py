import sqlite3
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)
DB_PATH = os.path.join(  BASE_DIR, "database", "database.db")

def connect_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn
def insert_product(produto):
    conn = connect_db()

    url = produto["url"]
    title = produto["titulo"]
    last_price = produto["preco"]

    store = produto["store"]    
    desconto = produto["desconto"]
    preco_total = produto["preco_total"]


    cursor = conn.cursor()
    cursor.execute(""" INSERT INTO products (url, title, last_price, store, desconto, preco_total, created_at) VALUES (?, ?, ?, ?, ?, ?, ?) """, (url, title, last_price, store, desconto, preco_total, "now()"))
    conn.commit()
    conn.close()

def update_product_price(url, new_price):
    conn = connect_db()

    cursor = conn.cursor()
    cursor.execute(""" UPDATE products SET last_price = ? WHERE url = ? """, (new_price, url))
    conn.commit()
    conn.close()

def get_product_by_url(url):
    conn = connect_db()

    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM products WHERE url = ? """, (url,))
    product = cursor.fetchone()
    conn.close()

    return product

def get_all_products():
    conn = connect_db()

    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM products """)
    products = cursor.fetchall()
    conn.close()

    return products