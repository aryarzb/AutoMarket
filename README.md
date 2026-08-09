# 🚗 AutoMarket

AutoMarket is a Django-based web application for buying and selling cars.

The project is designed as a simple car marketplace where users can create accounts, manage their profiles, and browse or add car listings.

## ✨ Features

* 👤 User registration and authentication
* 🔐 User login and logout
* 👤 User profiles
* 🚘 Add new car listings
* 📋 Browse available cars
* 🔎 View detailed car information
* 🖼️ Support for car images
* 🎨 Custom HTML and CSS templates
* 🗄️ Database management using Django ORM

## 🛠️ Technologies

* Python 3
* Django
* HTML5
* CSS3
* SQLite
* Git & GitHub

## 📁 Project Structure

```text
AutoMarket/
│
├── AutoMarket/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── cars/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── templates/
│   ├── accounts/
│   ├── cars/
│   └── base.html
│
├── static/
│
├── manage.py
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/aryarzb/AutoMarket.git
```

### 2. Navigate to the project directory

```bash
cd AutoMarket
```

### 3. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

### 5. Install the required packages

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install Django manually:

```bash
pip install django
```

## 🗄️ Database Setup

Run the Django migrations:

```bash
python manage.py migrate
```

If you make changes to the models, create new migrations with:

```bash
python manage.py makemigrations
```

Then apply them:

```bash
python manage.py migrate
```

## 👨‍💻 Create a Superuser

To access the Django administration panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal to set the username, email, and password.

## 🚀 Running the Project

Start the Django development server:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

The Django administration panel is available at:

```text
http://127.0.0.1:8000/admin/
```

## 🔒 Security

This project is currently intended for development and educational purposes.

Sensitive files and local development files should not be committed to the repository.

The following files and directories are excluded using `.gitignore`:

* `.venv/`
* `__pycache__/`
* `*.pyc`
* `db.sqlite3`
* `media/`
* `.idea/`
* `.vscode/`
* `.env`

Before deploying the application to production, make sure to:

* Set `DEBUG = False`
* Use a secure `SECRET_KEY`
* Configure `ALLOWED_HOSTS`
* Use a production-ready database
* Configure static and media files properly
* Store sensitive configuration in environment variables

## 📌 Project Status

🚧 **In Development**

AutoMarket is currently under development, and new features and improvements will be added over time.

## 🎯 Future Improvements

* 🔍 Advanced car search and filtering
* 💰 Price range filtering
* 📍 Location-based car listings
* ❤️ Favorite cars
* 💬 Messaging between buyers and sellers
* ⭐ User ratings and reviews
* 📱 Responsive mobile-friendly design
* 🖼️ Multiple images for each car
* 🔑 Improved authentication and authorization
* 🚀 Production deployment

## 📚 Purpose

This project was created as a learning project to practice:

* Django development
* Python backend development
* Database design
* Django ORM
* User authentication
* HTML and CSS
* Git and GitHub
* Web application architecture

## 👨‍💻 Author

**Arya Rouzbahani**

GitHub: [@aryarzb](https://github.com/aryarzb)

---

⭐ If you find this project useful, feel free to star the repository!
