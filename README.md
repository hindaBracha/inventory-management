# Inventory Management System

A robust and efficient Inventory Management System built with Django and Python. This system allows businesses and individuals to manage their inventory with ease, offering features to add, update, and remove items from stock. The project utilizes a relational database to maintain the integrity of inventory data and provides an intuitive API for seamless integration.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation and Setup](#installation-and-setup)
5. [How to Use](#how-to-use)
6. [Technologies Used](#technologies-used)
7. [UI/UX Design](#uiux-design)
8. [Contributing](#contributing)
9. [License](#license)
10. [Contact](#contact)

---

## Project Overview

The Inventory Management System is designed to help organizations and individuals efficiently manage their inventory through a clean and straightforward interface. The system supports basic inventory management functions such as adding, editing, and deleting products and categories.

This project was created with scalability and usability in mind, making it easy for users to track product details and manage stock levels effectively.

---

## Features

- **Add, Edit, and Delete Products**: Users can easily manage their product listings.
- **Product Categories**: Products are organized into categories for easy tracking.
- **Inventory Tracking**: Track quantities and prices of each product.
- **Django Admin Interface**: A powerful and user-friendly interface to manage all inventory data.
- **RESTful API**: Easily extend the system by interacting with the database programmatically.

---

## Requirements

To run the Inventory Management System on your local machine, you’ll need to have the following installed:

- **Python**: Version 3.8 or higher.
- **Django**: Version 5.1.4 or higher.
- **Database**: SQLite is used by default but can be configured to use other databases (e.g., PostgreSQL, MySQL).

---

## Installation and Setup

### Step 1: Clone the Repository

Begin by cloning this repository to your local machine:

```bash
git clone https://github.com/username/inventory-management.git
```

### Step 1: Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies:

```bash
cd inventory-management
python -m venv venv
```

### Step 3: Install Dependencies

Activate the virtual environment and install the required packages:

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

Then install the required packages:

```bash
pip install -r requirements.txt
```

### Step 4: Run Database Migrations

Set up the database by applying the migrations:

```bash
python manage.py migrate
```

### Step 5: Create a Superuser (Admin)

To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the instructions to set up your admin credentials.

### Step 6: Start the Development Server

Run the Django development server:

```bash
python manage.py runserver
```

The server will start at http://127.0.0.1:8000/. You can now access the application and the admin panel at http://127.0.0.1:8000/admin.

---

## How to Use

Once the server is running:

### Log in to the Django Admin Panel:

- Navigate to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).
- Log in using the superuser credentials you created.

### Manage Inventory:

- Add, edit, or delete products through the admin interface.
- Create categories to organize products.

### Access the API:

- The system provides a RESTful API for interacting with the inventory data programmatically.
- API endpoints are available for managing products, categories, and stock levels.

---

## Technologies Used

- **Python**: Programming language used to build the system.
- **Django**: Web framework that powers the application.
- **SQLite**: Default database (can be swapped for PostgreSQL, MySQL, etc.).
- **Django REST Framework**: For building the API (if applicable).

---

## UI/UX Design

The **Inventory Management System** was designed with a strong focus on **usability** and **visual clarity**. Below are the key principles followed during the UI/UX design process:

### 1. **Clean and Intuitive Layout**:
   The system's interface is clean, with a minimalist approach that ensures users can easily navigate the platform without feeling overwhelmed. 
   
   - The **Admin Panel** is the primary interface, with a left-side navigation bar and content areas for managing products, categories, and stock levels.
   - **Product and Category Cards** are displayed in a grid layout for easy access and quick data manipulation.
   - **Buttons and Forms**: All forms and buttons are designed to be large, visible, and easy to interact with, ensuring a smooth user experience even on mobile devices.

### 2. **Responsive Design**:
   - The application is fully responsive, adjusting seamlessly across various screen sizes, from desktops to tablets and smartphones. This ensures that inventory management is accessible on-the-go.

### 3. **Consistent Visual Hierarchy**:
   - Important actions (such as "Add Product" or "Delete Product") are highlighted with clear and distinct colors, allowing users to quickly locate critical options.
   - Data tables and charts are arranged logically, with bold headings and clear labeling, ensuring easy scanning of data.

### 4. **Real-Time Feedback**:
   - Interactive elements such as buttons and forms provide **immediate feedback**. For instance, after adding a product, the system offers a confirmation message or error alert, ensuring users understand the result of their actions.

### 5. **User-Centered Design**:
   - The system is built with the user in mind, ensuring that all interactions are streamlined. The interface minimizes the number of clicks required to perform an action, with easy navigation between sections.
   
   - The design also takes into account accessibility, ensuring that text is legible, and interactive elements are clearly distinguishable.

---

## Contributing

We welcome contributions to this project! If you have suggestions or improvements, feel free to open a pull request or submit an issue.

### How to Contribute:

1. Fork the repository.
2. Clone your fork to your local machine.
3. Create a new branch for your feature or fix.
4. Make your changes.
5. Test your changes.
6. Commit your changes and push them to your fork.
7. Open a pull request to the main repository.

---

## License

This project is licensed under the **MIT License**.

---

## Contact

For any questions, feel free to reach out via email or open an issue in the GitHub repository.

- **GitHub Repository**: [https://github.com/hindaBracha/inventory-management](https://github.com/hindaBracha/inventory-management)
- **Email**: hinda40311@gmail.com
```







