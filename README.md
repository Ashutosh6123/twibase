# Twibase - A Mini Twitter Clone

Twibase is a full-stack Django web application that mimics core features of Twitter, allowing users to register, login, post tweets (with optional images), edit or delete them, and view all tweets in a responsive interface.

## 🔧 Features

- ✅ User Authentication (Register/Login/Logout)
- ✍️ Create, Edit & Delete Tweets
- 🖼️ Upload Images with Tweets
- 🧠 Form validation and CSRF protection
- 🖥️ Responsive UI with Bootstrap 5
- 📁 Media file handling with Django's `MEDIA_URL` and `MEDIA_ROOT`
- 🛠️ Django Admin Panel support

## 🛠️ Tech Stack

- **Backend**: Django 5.2
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Authentication**: Django's built-in auth system

## 📁 Project Structure

```
twipost-main/
├── .gitignore                   # Git ignore rules
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── venv/                       # Virtual environment (auto-generated)
└── src/                        # Source code directory
    └── twipost/                # Django project root
        ├── manage.py           # Django management script
        ├── db.sqlite3          # SQLite database
        ├── static/             # Static files (CSS, JS, images)
        ├── media/              # User-uploaded files
        │   └── photos/         # Tweet images
        ├── templates/          # Global templates
        │   ├── layout.html     # Base template
        │   └── registration/   # Authentication templates
        ├── tweet/              # Main Django app
        │   ├── models.py       # Data models
        │   ├── views.py        # Business logic
        │   ├── forms.py        # Django forms
        │   ├── urls.py         # App URL patterns
        │   ├── admin.py        # Admin configuration
        │   ├── templates/      # App-specific templates
        │   └── migrations/     # Database migrations
        └── twipost/            # Django project settings
            ├── settings.py     # Project configuration
            ├── urls.py         # Main URL routing
            └── wsgi.py         # WSGI application
```

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/twibase.git
cd twipost-main
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Navigate to Django Project

```bash
cd src/twipost
```

### 5. Run Database Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

### 8. Access the Application

- **Main Application**: http://127.0.0.1:8000/tweet/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 🎯 Usage

1. **Register**: Create a new account at `/tweet/register/`
2. **Login**: Sign in at `/accounts/login/`
3. **Create Tweets**: Click "Create a tweet" on the home page
4. **Upload Images**: Add optional images to your tweets
5. **Edit/Delete**: Manage your own tweets with edit/delete options
6. **Admin Panel**: Access Django admin for advanced management

## 🔧 Development

- **Django Version**: 5.2.3
- **Python Version**: 3.8+
- **Database**: SQLite (default), can be changed in `settings.py`
- **Static Files**: Stored in `src/twipost/static/`
- **Media Files**: User uploads in `src/twipost/media/photos/`

## 📝 License

This project is open source and available under the MIT License.
