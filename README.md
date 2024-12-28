# The Inventory Management System
The Inventory Management System is designed to help organizations and individuals efficiently manage their inventory through a clean and straightforward interface. The system supports basic inventory management functions such as adding, editing, and deleting products and categories while incorporating an intelligent chat feature to streamline communication with the database.

This project was created with scalability and usability in mind, making it easy for users to track product details, manage stock levels effectively, and interact with the system via an integrated chat interface.

## Features
- **Add, Edit, and Delete Products**: Users can easily manage their product listings.
- **Product Categories**: Products are organized into categories for easy tracking.
- **Inventory Tracking**: Track quantities and prices of each product.
- **Django Admin Interface**: A powerful and user-friendly interface to manage all inventory data.
- **RESTful API**: Easily extend the system by interacting with the database programmatically.
- **Intelligent Chat Interface**: A chat feature that fetches data from the database in real-time, enhancing user interaction.
- **Automated Daily Reports**: Automatically generate and send daily inventory reports via email using Celery and Celery Beat.

## Requirements
To run the Inventory Management System on your local machine, you’ll need to have the following installed:

- **Python**: Version 3.8 or higher.
- **Django**: Version 5.1.4 or higher.
- **Celery**: For asynchronous task processing.
- **Redis**: As a message broker for Celery.
- **Database**: SQLite is used by default but can be configured to use other databases (e.g., PostgreSQL, MySQL).

## Installation and Setup
### Step 1: Clone the Repository
```bash
git clone https://github.com/hindaBracha/inventory-management.git
```

### Step 2: Create a Virtual Environment
```bash
cd inventory-management  
python -m venv venv
```

### Step 3: Install Dependencies
For Windows:
```bash
venv\Scripts\activate
```
For macOS/Linux:
```bash
source venv/bin/activate
```
Install the required packages:
```bash
pip install -r requirements.txt
```

### Step 4: Run Database Migrations
```bash
python manage.py migrate
```

### Step 5: Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```

### Step 6: Start Redis Server
Make sure Redis is installed and running on your machine. You can start it with:
```bash
redis-server
```

### Step 7: Start Celery Worker and Celery Beat
Run Celery Worker:
```bash
celery -A inventory_management worker --loglevel=info
```
Run Celery Beat for task scheduling:
```bash
celery -A inventory_management beat --loglevel=info
```

### Step 8: Start the Development Server
```bash
python manage.py runserver
```

## How to Use
Once the server is running:

1. **Log in to the Django Admin Panel**: Navigate to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and log in using the superuser credentials.
2. **Manage Inventory**: Add, edit, or delete products and categories through the admin interface.
3. **Interact with the Chat Feature**: Use the intelligent chat to fetch product or inventory data directly from the database.
4. **Access the API**: Programmatically interact with inventory data through the RESTful API.
5. **Daily Reports**:
   - The system automatically generates and sends a daily inventory report at midnight.
   - The report includes product names and their stock levels.
   - Reports are sent via email to the configured recipient.

## Technologies Used
- **Python**: Programming language used to build the system.
- **Django**: Web framework that powers the application.
- **Celery**: For handling asynchronous tasks.
- **Redis**: Message broker for Celery tasks.
- **SQLite**: Default database (can be swapped for PostgreSQL, MySQL, etc.).
- **HTML, CSS, JavaScript**: Technologies used for building the intuitive frontend interface.
- **Django REST Framework**: For building the API.

## Automated Task Scheduling with Celery and Celery Beat
The system uses **Celery** for asynchronous task processing and **Celery Beat** for scheduling periodic tasks. Specifically:

- A **daily inventory report** is generated and emailed at midnight.
- The task fetches all product data, compiles it into a report, and sends it via email to a predefined recipient.

To configure this feature:
1. Ensure Redis is running as the Celery message broker.
2. Start both the Celery Worker and Celery Beat processes.
3. Update the email settings in the Django project's `settings.py` file to enable email delivery.

Example Celery task for daily reporting:
```python
from celery import shared_task
from django.core.mail import send_mail
from .models import Product

@shared_task
def send_daily_report():
    products = Product.objects.all()
    report = "Daily Report\n\n"
    for product in products:
        report += f"Product: {product.name}, Stock: {product.stock}\n"

    send_mail(
        'Daily Inventory Report',
        report,
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
```

## UI/UX Design
The system is designed with the following principles:
- **Clean and Intuitive Layout**: Minimalist design for easy navigation.
- **Responsive Design**: Accessible across devices.
- **Real-Time Feedback**: Instant updates for actions like adding products.
- **User-Centered Design**: Streamlined workflows and accessibility.

## Contributing
We welcome contributions to this project! If you have suggestions or improvements, feel free to open a pull request or submit an issue.

### How to Contribute:
1. Fork the repository.
2. Clone your fork to your local machine.
3. Create a new branch for your feature or fix.
4. Make and test your changes.
5. Commit and push to your fork.
6. Open a pull request to the main repository.

## License
This project is licensed under the MIT License.

## Contact
For any questions, feel free to reach out via email or open an issue in the GitHub repository.

- **GitHub Repository**: [Inventory Management System](https://github.com/hindaBracha/inventory-management)
- **Email**: hinda40311@gmail.com

