### The Inventory Management System  

The Inventory Management System is designed to help organizations and individuals efficiently manage their inventory through a clean and straightforward interface. The system supports basic inventory management functions such as adding, editing, and deleting products and categories while incorporating an intelligent chat feature to streamline communication with the database.

This project was created with scalability and usability in mind, making it easy for users to track product details, manage stock levels effectively, and interact with the system via an integrated chat interface.

---

### Features  

- **Add, Edit, and Delete Products**: Users can easily manage their product listings.  
- **Product Categories**: Products are organized into categories for easy tracking.  
- **Inventory Tracking**: Track quantities and prices of each product.  
- **Django Admin Interface**: A powerful and user-friendly interface to manage all inventory data.  
- **RESTful API**: Easily extend the system by interacting with the database programmatically.  
- **Intelligent Chat Interface**: A chat feature that fetches data from the database in real-time, enhancing user interaction.  

---

### Requirements  

To run the Inventory Management System on your local machine, you’ll need to have the following installed:  

- **Python**: Version 3.8 or higher.  
- **Django**: Version 5.1.4 or higher.  
- **Database**: SQLite is used by default but can be configured to use other databases (e.g., PostgreSQL, MySQL).  

---

### Installation and Setup  

**Step 1**: Clone the Repository  

```bash  
git clone https://github.com/hindaBracha/inventory-management.git  
```  

**Step 2**: Create a Virtual Environment  

```bash  
cd inventory-management  
python -m venv venv  
```  

**Step 3**: Install Dependencies  

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

**Step 4**: Run Database Migrations  

```bash  
python manage.py migrate  
```  

**Step 5**: Create a Superuser (Admin)  

```bash  
python manage.py createsuperuser  
```  

**Step 6**: Start the Development Server  

```bash  
python manage.py runserver  
```  

---

### How to Use  

Once the server is running:  

- **Log in to the Django Admin Panel**: Navigate to `http://127.0.0.1:8000/admin` and log in using the superuser credentials.  
- **Manage Inventory**: Add, edit, or delete products and categories through the admin interface.  
- **Interact with the Chat Feature**: Use the intelligent chat to fetch product or inventory data directly from the database.  
- **Access the API**: Programmatically interact with inventory data through the RESTful API.  

---

### Technologies Used  

- **Python**: Programming language used to build the system.  
- **Django**: Web framework that powers the application.  
- **SQLite**: Default database (can be swapped for PostgreSQL, MySQL, etc.).  
- **HTML, CSS, JavaScript**: Technologies used for building the intuitive frontend interface.  
- **Django REST Framework**: For building the API.  

---

### UI/UX Design  

The system is designed with the following principles:  

- **Clean and Intuitive Layout**: Minimalist design for easy navigation.  
- **Responsive Design**: Accessible across devices.  
- **Real-Time Feedback**: Instant updates for actions like adding products.  
- **User-Centered Design**: Streamlined workflows and accessibility.  

---

### Contributing  

We welcome contributions to this project! If you have suggestions or improvements, feel free to open a pull request or submit an issue.  

**How to Contribute**:  
1. Fork the repository.  
2. Clone your fork to your local machine.  
3. Create a new branch for your feature or fix.  
4. Make and test your changes.  
5. Commit and push to your fork.  
6. Open a pull request to the main repository.  

---

### License  

This project is licensed under the MIT License.  

---

### Contact  

For any questions, feel free to reach out via email or open an issue in the GitHub repository.  

- **GitHub Repository**: [Inventory Management System](https://github.com/hindaBracha/inventory-management)  
- **Email**: hinda40311@gmail.com  