# Flask Order Handling System

A simple backend application built with **Flask** for managing and tracking customer orders. The system allows you to create, edit, delete, and mark orders as delivered. All actions are logged for auditing.

---

## Features

- **Add New Orders**  
  Create orders with unique order IDs, delivery details, and customer information.

- **Edit Orders**  
  Update existing order details.

- **Delete Orders**  
  Remove orders from the system.

- **Mark as Delivered**  
  Change the status of an order from "Ongoing" to "Delivered".

- **Action Logging**  
  Every action (create, edit, delete, deliver) is recorded in an action log with a timestamp and performer name.

- **Minimal HTML Interface**  
  Basic forms and tables using Jinja2 templates. Optional styling added with CSS for better readability.

---

## Tech Stack

- Python 3
- Flask 3.x
- SQLite3 (built-in database)
- Jinja2 templates (for HTML rendering)

---

## Project Structure


---

## Installation & Running

1. **Clone the repository**  
   git clone https://github.com/Minha-Attique/flask-order-system.git
   cd flask-order-system

2. **Create a virtual environment**  
    python -m venv venv
    venv\Scripts\activate     # For Windows

3. **Install dependencies**  
    pip install -r requirements.txt 

4. **Run the app**  
    python app.py 

5. **Open in browser**  
    Visit `http://127.0.0.1:5000` in your browser.

---

## How It Works (Approach)

- The app uses **Flask** routes to serve HTML pages with forms and tables.
- A **SQLite database** stores order data and action logs.
- The app initializes the DB using a helper function before serving requests.
- Templates use **Jinja2** for rendering and basic structure (`base.html` as layout).
- All CRUD actions are implemented via HTML forms.
- Logs are inserted automatically when changes occur.
- Optional styles are applied via `static/styles.css` for better user experience.

---

## Optional: GitHub Pages

This repository includes a `docs/index.md` file for basic documentation viewable at:
**[GitHub Pages Link](https://Minha-Attique.github.io/flask-order-system/)**

---

## Author

Minha-Attique




