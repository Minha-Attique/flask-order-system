from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id TEXT UNIQUE,
            items INTEGER,
            delivery_date TEXT,
            sender TEXT,
            recipient TEXT,
            address TEXT,
            status TEXT DEFAULT 'Ongoing'
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT,
            performed_by TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Routes
@app.route('/')
def index():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("SELECT * FROM orders")
    orders = c.fetchall()
    conn.close()
    return render_template('orders.html', orders=orders)

@app.route('/add', methods=['GET', 'POST'])
def add_order():
    if request.method == 'POST':
        order_id = request.form['order_id']
        items = request.form['items']
        delivery_date = request.form['delivery_date']
        sender = request.form['sender']
        recipient = request.form['recipient']
        address = request.form['address']
        conn = sqlite3.connect('orders.db')
        c = conn.cursor()
        c.execute("INSERT INTO orders (order_id, items, delivery_date, sender, recipient, address) VALUES (?, ?, ?, ?, ?, ?)",
                  (order_id, items, delivery_date, sender, recipient, address))
        c.execute("INSERT INTO logs (action, performed_by, timestamp) VALUES (?, ?, ?)",
                  (f"Created order {order_id}", "Admin", datetime.now()))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_order.html')

@app.route('/edit/<order_id>', methods=['GET', 'POST'])
def edit_order(order_id):
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    if request.method == 'POST':
        items = request.form['items']
        delivery_date = request.form['delivery_date']
        sender = request.form['sender']
        recipient = request.form['recipient']
        address = request.form['address']
        c.execute('''
            UPDATE orders
            SET items=?, delivery_date=?, sender=?, recipient=?, address=?
            WHERE order_id=?
        ''', (items, delivery_date, sender, recipient, address, order_id))
        c.execute("INSERT INTO logs (action, performed_by, timestamp) VALUES (?, ?, ?)",
                  (f"Edited order {order_id}", "Admin", datetime.now()))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    c.execute("SELECT * FROM orders WHERE order_id=?", (order_id,))
    order = c.fetchone()
    conn.close()
    return render_template('edit_order.html', order=order)

@app.route('/delete/<order_id>')
def delete_order(order_id):
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("DELETE FROM orders WHERE order_id=?", (order_id,))
    c.execute("INSERT INTO logs (action, performed_by, timestamp) VALUES (?, ?, ?)",
              (f"Deleted order {order_id}", "Admin", datetime.now()))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/deliver/<order_id>')
def mark_delivered(order_id):
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("UPDATE orders SET status='Delivered' WHERE order_id=?", (order_id,))
    c.execute("INSERT INTO logs (action, performed_by, timestamp) VALUES (?, ?, ?)",
              (f"Marked order {order_id} as Delivered", "Admin", datetime.now()))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/logs')
def view_logs():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("SELECT * FROM logs ORDER BY timestamp DESC")
    logs = c.fetchall()
    conn.close()
    return render_template('logs.html', logs=logs)

# At the bottom of app.py

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

