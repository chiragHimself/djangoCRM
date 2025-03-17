# 📝 Django CRM - Customer Relationship Management System

Welcome to **DjangoCRM** – A powerful yet simple Customer Relationship Management (CRM) system built using Django and MySQL. 🔥

With DjangoCRM, users can register, log in securely, and manage customer data effortlessly – including adding, updating, and deleting records.

## 🚀 Features

✅ **User Authentication** – Secure login & registration using Django Authentication. 🔒  
✅ **Manage Customers** – Add, update, and delete customer records with ease. 📋  
✅ **Django Forms** – Used for handling customer data efficiently. 📝  
✅ **MySQL Integration** – All data is stored in a MySQL database. 🗄️  
✅ **User-Friendly Dashboard** – View all customer data in an intuitive UI. 🎨  
✅ **Fully Responsive** – Bootstrap-powered UI for great user experience. 📱💻  

## 📸 Screenshots

🚀 *[Include some screenshots of your app’s UI here]*

## ⚙️ Installation Guide

Follow these steps to get DjangoCRM up and running on your local machine:

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/chiragHimself/djangoCRM.git
cd djangoCRM
```

### 2️⃣ Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up MySQL Database

Create a MySQL database and update the `settings.py` file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5️⃣ Run Migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create a Superuser (Admin Access)

```sh
python manage.py createsuperuser
```

### 7️⃣ Start the Development Server

```sh
python manage.py runserver
```

Now visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser. 🚀

## 👤 User Authentication

- **Register** – New users can sign up.  
- **Login** – Secure authentication with Django.  
- **Logout** – End the session securely.  

## 🎯 How It Works

1️⃣ **Login or Register** 🛡️  
2️⃣ **View all customer records** 📊  
3️⃣ **Add new customers** ➕  
4️⃣ **Edit & update details** ✏️  
5️⃣ **Delete unwanted records** 🗑️  

## 🎨 Tech Stack

| **Technology** | **Description** |
|---------------|---------------|
| **Django** | Backend framework 🛠️ |
| **MySQL** | Database system 🗄️ |
| **Bootstrap** | Frontend styling 🎨 |
| **Django Forms** | Handling forms & validation ✅ |
| **HTML/CSS/JS** | User Interface 💻 |

## 🛠️ Contributing

🚀 Want to improve DjangoCRM? Contributions are welcome!

1. Fork this repo  
2. Create a new branch (`git checkout -b feature-xyz`)  
3. Commit your changes (`git commit -m "Added a new feature"`)  
4. Push to your branch (`git push origin feature-xyz`)  
5. Create a Pull Request 🎉  

## 📜 License

📝 This project is open-source and licensed under the **MIT License**.

## 💬 Need Help?

📩 Feel free to reach out if you have any questions or suggestions!

Give this repo a ⭐ if you find it useful! 🚀
