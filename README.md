# Flask Order Handling System

A simple backend application built with **Flask** for managing and tracking customer orders. The system allows you to create, edit, delete, and mark orders as delivered. All actions are logged for auditing.

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
  Basic forms and tables using Jinja2 templates, no CSS or JavaScript required.

---

## 🛠 Tech Stack

- Python 3
- Flask 3.x
- SQLite3 (built-in database)
- Jinja2 templates (for HTML rendering)

---

## Project Structure

