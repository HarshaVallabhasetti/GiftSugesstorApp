import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('gifts.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Create the gifts table
cur.execute('''
CREATE TABLE IF NOT EXISTS gifts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price INTEGER NOT NULL,
    gender TEXT NOT NULL
)
''')

# Insert sample data into the gifts table
gifts = [
    ('Book: "The Great Gatsby"', 'Books', 150, 'Unisex'),
    ('Book: "Romeo And Juliet"', 'Books', 250, 'Unisex'),
    ('Book: "Harry Potter" Complete set', 'Books', 2780, 'Unisex'),
    ('Wireless Headphones', 'Electronics', 1200, 'Unisex'),
    ('Apple Earpods', 'Electronics', 18000, 'Unisex'),
    ('Table Fan', 'Electronics', 2600, 'Unisex'),
    ('Cooking Set', 'Kitchen', 500, 'Female'),
    ('Air Fryer', 'Kitchen', 5000, 'Unisex'),
    ('Toaster', 'Kitchen', 1099, 'Unisex'),
    ('Coffee Maker', 'Kitchen', 3000, 'Unisex'),
    ('Yoga Mat', 'Fitness', 200, 'Unisex'),
    ('Pull Up Bar', 'Fitness', 1780, 'Unisex'),
    ('Dumbbells', 'Fitness', 2499, 'Unisex'),
    ('Hand Grip', 'Fitness', 300, 'Unisex'),
    ('Sweater', 'Clothing', 800, 'Unisex'),
    ('Scarf', 'Clothing', 400, 'Unisex'),
    ('Jacket', 'Clothing', 1500, 'Unisex'),
    ('Board Game: Chief Choice', 'Games', 1500, 'Unisex'),
    ('Board Game: Monopoly', 'Games', 1500, 'Unisex'),
    ('Valorant: VP', 'Games', 2100, 'Unisex'),
    ("Men's Wallet", 'Accessories', 500, 'Male'),
    ("Women's Purse", 'Accessories', 500, 'Female'),
    ('Titan Watch', 'Accessories', 7000, 'Female'),
    ('Photo Frames', 'House Decor', 1500, 'Unisex'),
    ('Flower Vase', 'House Decor', 299, 'Unisex'),
    ('Led Strip Light', 'House Decor', 498, 'Unisex'),
    ('Starbucks Gift Card', 'Gift Cards', 294, 'Unisex'),
    ('Ajio Gift Card', 'Gift Cards', 500, 'Unisex'),
    ('Amazon Gift Card', 'Gift Cards', 500, 'Unisex')
]

cur.executemany('''
INSERT INTO gifts (name, category, price, gender) VALUES (?, ?, ?, ?)
''', gifts)

# Commit the changes and close the connection
conn.commit()
conn.close()
