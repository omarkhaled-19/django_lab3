# 🛍️ Django Lab3 – Products App + Categories app (using the Django Forms)

This project is a simple Django application to manage products with **CRUD operations** (Create, Read, Update, Delete) using **MySQL** database integration and image upload functionality. 

The key feature of this project is that it's built **with Django Forms** applied to the Categories app with `request.POST` and `request.FILES`.

## ✅ Prerequisites

Before starting, ensure you have the following installed:

- **Python 3.8+**
- **MySQL Server** 
- **Git** 

## 🚀 Installation Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/omarkhaled-19/django_lab2_wihtout_forms.git
cd django-lab2-products
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Required Python Packages
```bash
pip install django
pip install pillow
pip install mysqlclient
```

> **Note**: If you encounter issues installing `mysqlclient`, see the Troubleshooting section below.

## 🗄️ Database Setup

### Step 1: Start MySQL Server
Make sure your MySQL server is running on your machine.

### Step 2: Create Database and User
Open MySQL command line or MySQL Workbench and run:

```sql
-- Create database
CREATE DATABASE productsdb;

-- Create user (optional - you can use root)
CREATE USER 'django'@'localhost' IDENTIFIED BY 'password';

-- Grant privileges
GRANT ALL PRIVILEGES ON productsdb.* TO 'django'@'localhost';
FLUSH PRIVILEGES;
```

### Step 3: Verify Database Settings
Your database should have these settings:
- **Database Name**: `productsdb`
- **Username**: `django` (or `root` if you prefer)
- **Password**: `password` (or your root password)
- **Host**: `localhost`
- **Port**: `3306` (default MySQL port)

## ⚙️ Project Configuration

### Step 1: Configure Database Settings
In your `settings.py`, ensure the database configuration matches:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'productsdb',
        'USER': 'django',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Step 2: Configure Media Files
Ensure these settings are in your `settings.py`:

```python
import os

# Media files (for image uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

## 🏃‍♂️ Running the Project

### Step 1: Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 2: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### Step 3: Run Development Server
```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

### Step 4: Access Admin Panel (Optional)
Visit `http://127.0.0.1:8000/admin/` and login with your superuser credentials.

## ✨ Features

- ✅ **Create Products**: Add new products with name, description, price, and image
- ✅ **View Products**: Display all products in a clean list format
- ✅ **Update Products**: Edit existing product information
- ✅ **Delete Products**: Remove products from the database
- ✅ **Image Upload**: Upload and display product images
- ✅ **MySQL Integration**: Full database persistence
- ✅ **Admin Panel**: Django admin interface for easy management


## 🔧 Troubleshooting

### MySQL Connection Issues
If you get database connection errors:
1. Ensure MySQL server is running
2. Verify database name, username, and password
3. Check if the database `productsdb` exists

### mysqlclient Installation Issues

**On Windows:**
```bash
pip install mysqlclient
# If it fails, try:
pip install wheel
pip install mysqlclient
```

**On macOS:**
```bash
brew install mysql
pip install mysqlclient
```

**On Ubuntu/Linux:**
```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
pip install mysqlclient
```

### Media Files Not Displaying
Ensure your main `urls.py` includes media URL configuration:

```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
