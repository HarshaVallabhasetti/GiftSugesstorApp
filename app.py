from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('gifts.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest():
    likes = request.form.get('likes').lower()
    max_price = request.form.get('max_price', type=int)
    gender = request.form.get('gender')

    print("Likes:", likes)
    print("Max Price:", max_price)
    print("Gender:", gender)

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM gifts WHERE
    LOWER(category) LIKE ? AND
    price <= ? AND
    (gender = ? OR gender = 'Unisex')
    ''', ('%' + likes + '%', max_price, gender))
    
    gifts = cur.fetchall()
    conn.close()

    print("Gifts Found:", len(gifts))
    for gift in gifts:
        print(gift['name'], gift['price'])

    return render_template('result.html', gifts=gifts)

if __name__ == '__main__':
    app.run(debug=True)
