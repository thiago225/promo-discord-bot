import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    title TEXT,
    last_price REAL
)
""")

# add essas coluna store, desconto, preco_total updated_at e created_at na tabela products
# cursor.execute("""
# ALTER TABLE products
#   ADD COLUMN store TEXT
# """)
# cursor.execute("""
# ALTER TABLE products
#   ADD COLUMN desconto TEXT
# """)
# cursor.execute("""
# ALTER TABLE products
#   ADD COLUMN preco_total REAL
# """)
# cursor.execute("""
# ALTER TABLE products
#   ADD COLUMN updated_at DATETIME
# """)
cursor.execute("""
ALTER TABLE products
  ADD COLUMN created_at DATETIME
""")

conn.commit()
conn.close()

print("Banco criado.")