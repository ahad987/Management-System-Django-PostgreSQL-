# Management System (Django and PostgreSQL)

A Django-based Management System built with **Django** and **PostgreSQL** featuring a **Custom User Authentication System** and complete **CRUD operations** for Employees, Products, and Students.

---

## 🚀 Features

### 🔐 Authentication Module

* Custom User Model implementation
* User Registration (Signup)
* User Login (Signin)
* User Logout
* Authentication-based access control
* Only authenticated users can access management modules

---

## 🛠 Technology Stack

* **Backend:** Django
* **Database:** PostgreSQL
* **Frontend:** HTML, CSS, Bootstrap
* **Authentication:** Django Custom User Model

---

## 📂 Project Modules

### 1. Employee Management

#### Model: Employee

| Field      | Type         |
| ---------- | ------------ |
| Name       | CharField    |
| Email      | EmailField   |
| Phone      | CharField    |
| Department | CharField    |
| Salary     | DecimalField |

#### Operations

* Create Employee
* View Employee List
* Update Employee
* Delete Employee

---

### 2. Product Management

#### Model: Product

| Field        | Type         |
| ------------ | ------------ |
| Product Name | CharField    |
| Category     | CharField    |
| Price        | DecimalField |
| Quantity     | IntegerField |
| Description  | TextField    |

#### Operations

* Create Product
* View Product List
* Update Product
* Delete Product

---

### 3. Student Management

#### Model: Student

| Field       | Type         |
| ----------- | ------------ |
| Name        | CharField    |
| Roll Number | CharField    |
| Email       | EmailField   |
| Course      | CharField    |
| Semester    | IntegerField |

#### Operations

* Create Student
* View Student List
* Update Student
* Delete Student

---

## 📋 Functional Requirements

### User Authentication

* Users can register an account.
* Registered users can log in.
* Unauthorized users cannot access protected pages.
* Authenticated users can perform CRUD operations.

### CRUD Functionality

Each module supports:

* Create Records
* Read/View Records
* Update Records
* Delete Records

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/management-system.git
cd management-system
```

### 2. Create Virtual Environment

```bash
python -m venv MyEnv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL Database

Create a PostgreSQL database and update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'management_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 📁 Suggested Project Structure

```text
management_system/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── employees/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── products/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── students/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── templates/
├── static/
├── manage.py
└── requirements.txt
```

---

## 🔒 Access Control

| User Status        | Access                    |
| ------------------ | ------------------------- |
| Guest User         | Login & Signup Pages Only |
| Authenticated User | Full CRUD Access          |
| Admin              | Full System Access        |

---

## 🎯 Learning Objectives

This project demonstrates:

* Django Custom User Model
* Authentication & Authorization
* PostgreSQL Integration
* CRUD Operations
* Django Forms
* Class-Based or Function-Based Views
* URL Routing
* Template Rendering
* Database Relationships and Management

---

## 📜 License

This project is developed for educational and learning purposes. Feel free to modify and extend it according to your requirements.

---

💡 Recommendation: Generate a requirements.txt file to track your dependencies:

```bash
pip freeze > requirements.txt
```

## 👤 Contact

**Abdul Ahad Chowdhury**
- GitHub: [@ahad987](https://github.com/ahad987)
- Email: [ahad987@gmail.com](mailto:ahad987@gmail.com)
- **LinkedIn:** [Your Name / Profile](https://www.linkedin.com/in/ahad1987/)
- **Facebook:** [ahadc](https://facebook.com)
- **WhatsApp:** [Message on WhatsApp](https://wa.me)
- **Phone:** [+880 1812148778](tel:+8801812148778)
- Project: [https://github.com/ahad987/Management-System-Django-PostgreSQL-](https://github.com/ahad987/Management-System-Django-PostgreSQL-)

---

<div align="center">Made with ❤️ by Abdul Ahad Chowdhury</div>

