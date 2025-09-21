
# 📚 AIMCA Library Management System

<div align="center">
  <img src="https://img.shields.io/badge/Django-5.2.4-green?logo=django" alt="Django Version" />
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" alt="Python Version" />
  <img src="https://img.shields.io/badge/Batch-26-orange" alt="Batch 26" />
</div>

<p align="center">
  <b>A modern Django-based library management system by Batch-26, AIMCA</b><br>
  <i>Efficiently manage books, members, and loans with analytics, automation, and a responsive dashboard.</i>
</p>

---

## 🚀 Quick Start

1. <b>
    ```bash
    git clone <[repository-url](https://github.com/shaanlabs/Aimca-lib.git</b>)>
    cd college-project
    ```
2. <b>Create & activate virtual environment</b>
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate.ps1  # Windows
    source venv/bin/activate      # macOS/Linux
    ```
3. <b>Install dependencies</b>
    ```bash
    pip install -r requirements.txt
    ```
4. <b>Run migrations</b>
    ```bash
    python manage.py makemigrations
    python manage.py migrate
[https://github.com/shaanlabs/Aimca-lib.git](https://github.com/shaanlabs/Aimca-lib.git)
    ```
    ```bash
    python manage.py createsuperuser
    # Follow prompts for credentials
    python manage.py runserver

---

## ✨ Features

- 📊 <b>Dashboard Analytics</b>: Real-time stats & charts
- 📚 <b>Book Management</b>: Add, edit, track inventory
- 👥 <b>Member Management</b>: Register students & faculty
- 📖 <b>Loan Tracking</b>: Borrow, return, overdue management
- 🔍 <b>Search & Filter</b>: Advanced search capabilities
- 📱 <b>Responsive Design</b>: Works on desktop & mobile

---

## 🛠️ Tech Stack
|-----------|--------------|
| Database  | SQLite3      |
| Frontend  | HTML5, CSS3, JS |
| Python    | 3.8+         |

---

<details>
<summary><b>Frontend Team</b></summary>

- <b>Lead:</b> Azharuddin Ali
- <b>Members:</b> Nada, Sidra, Hayyan
</details>

<details>

- <b>Lead:</b> Nashil Damudi
- <b>Members:</b> Sultan, Fahman, Fayha, Sayana, Bhumika
<summary><b>Guidance</b></summary>
- Deepa Ma’am

</details>

---

## 🌐 Access

- Main App: [http://localhost:8000/](http://localhost:8000/)
- Admin Panel: [http://localhost:8000/admin/](http://localhost:8000/admin/)
- Books: [http://localhost:8000/books/](http://localhost:8000/books/)
- Members: [http://localhost:8000/members/](http://localhost:8000/members/)

---


```text
college-project/
├── library_management/   # Django project settings
├── books/               # Books app
├── members/             # Members app
├── templates/           # HTML templates
├── static/              # Static files
├── manage.py            # Django management script
└── README.md            # This file
```

---


**Book**: title, author, isbn, year, quantity, available_quantity, timestamps

**Member**: name, email, phone, address, membership_date, is_active


---

## 🔧 Configuration


---



## 🧪 Testing

Test admin, book/member management, dashboard, and navigation as described above.

---

## 🔒 Security & Deployment
- Change SECRET_KEY, set DEBUG=False, use environment variables
- Use HTTPS, upgrade database for production
- See checklist in original README for more

---

## 🤝 Contributing
1. Fork the repo
2. Create a feature branch
3. Commit & push changes
4. Open a Pull Request

---

## 📝 License & Support

Developed by Batch-26 students of AIMCA for educational purposes.

For support: open an issue or contact the team.

---

<div align="center">
  <sub>Last Updated: July 2025 &nbsp;|&nbsp; Version: 1.0.0 &nbsp;|&nbsp; Django 5.2.4</sub>
</div>

## 🗄️ Database Models

### Book Model
- `title`: Book title (CharField, max_length=200)
- `author`: Book author (CharField, max_length=200)
- `isbn`: International Standard Book Number (CharField, max_length=13, unique)
- `publication_year`: Year of publication (IntegerField)
- `quantity`: Total number of copies (IntegerField, default=1)
- `available_quantity`: Available copies (IntegerField, default=1)
- `created_at`: Creation timestamp (DateTimeField, auto_now_add=True)
- `updated_at`: Last update timestamp (DateTimeField, auto_now=True)

### Member Model
- `name`: Member name (CharField, max_length=200)
- `email`: Email address (EmailField, unique)
- `phone`: Phone number (CharField, max_length=15)
- `address`: Address (TextField)
- `membership_date`: Membership start date (DateTimeField, auto_now_add=True)
- `is_active`: Active status (BooleanField, default=True)

### BookLoan Model
- `book`: Foreign key to Book model
- `member`: Foreign key to Member model
- `borrowed_date`: Date when book was borrowed (DateTimeField, auto_now_add=True)
- `due_date`: Due date for return (DateTimeField)
- `returned_date`: Actual return date (DateTimeField, null=True, blank=True)
- `status`: Loan status - 'borrowed', 'returned', 'overdue' (CharField, max_length=10)

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root for sensitive configuration:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### Django Settings
Key settings in `library_management/settings.py`:

```python
# Debug mode (set to False in production)
DEBUG = True

# Allowed hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Static files configuration
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## 🚨 Common Errors & Solutions

### 1. **ModuleNotFoundError: No module named 'django'**
**Error**: `ModuleNotFoundError: No module named 'django'`
**Solution**: 
```bash
# Activate virtual environment first
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # macOS/Linux

# Then install requirements
pip install -r requirements.txt
```

### 2. **Database Migration Errors**
**Error**: `django.db.utils.OperationalError: no such table`
**Solution**:
```bash
# Delete existing migrations and recreate
rm -rf books/migrations/0*.py
rm -rf members/migrations/0*.py
python manage.py makemigrations
python manage.py migrate
```

### 3. **Static Files Not Loading**
**Error**: CSS/JS files not loading (404 errors)
**Solution**:
```bash
# Collect static files
python manage.py collectstatic

# Check settings.py has correct static configuration
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

### 4. **Port Already in Use**
**Error**: `Error: That port is already in use.`
**Solution**:
```bash
# Use different port
python manage.py runserver 8001

# Or kill existing process
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:8000 | xargs kill -9
```

### 5. **Permission Errors (Windows)**
**Error**: `PermissionError: [Errno 13] Permission denied`
**Solution**:
```bash
# Run PowerShell as Administrator
# Or use different directory
cd C:\Users\YourUsername\Desktop
```

### 6. **Template Does Not Exist**
**Error**: `TemplateDoesNotExist at /`
**Solution**:
```bash
# Check template directory in settings.py
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],  # Make sure this exists
        'APP_DIRS': True,
    }
]

# Verify template files exist
ls templates/
```

### 7. **URL Pattern Not Found**
**Error**: `NoReverseMatch at /`
**Solution**:
```bash
# Check URL patterns in urls.py
# Ensure all URL names match in templates
# Run URL check
python manage.py check
```

### 8. **Database Lock Errors**
**Error**: `database is locked`
**Solution**:
```bash
# Close any database viewers
# Restart Django server
# If persistent, delete db.sqlite3 and remigrate
rm db.sqlite3
python manage.py migrate
```

## 🧪 Testing the Application

### 1. **Test Admin Interface**
- Go to http://localhost:8000/admin/
- Login with superuser credentials
- Add sample books and members

### 2. **Test Book Management**
- Navigate to Books section
- Add a new book
- Check if it appears in the list

### 3. **Test Member Management**
- Go to Members section
- Add a new member
- Verify member appears in the list

### 4. **Test Dashboard**
- Check if dashboard loads correctly
- Verify statistics are displayed
- Test navigation between sections

## 🔒 Security Considerations

### Production Deployment
1. **Change SECRET_KEY**: Generate a new secret key
2. **Set DEBUG=False**: Disable debug mode
3. **Use Environment Variables**: Store sensitive data in .env
4. **HTTPS**: Use SSL/TLS certificates
5. **Database**: Use PostgreSQL or MySQL instead of SQLite
6. **Static Files**: Serve via CDN or web server

### Security Checklist
- [ ] Change default admin credentials
- [ ] Use strong passwords
- [ ] Enable HTTPS
- [ ] Regular security updates
- [ ] Backup database regularly
- [ ] Monitor access logs

## 📊 Performance Optimization

### Database Optimization
```python
# Use select_related for foreign keys
books = Book.objects.select_related('author').all()

# Use prefetch_related for many-to-many
loans = BookLoan.objects.prefetch_related('member', 'book').all()
```

### Static Files
```bash
# Compress static files
python manage.py collectstatic --noinput
```

### Caching
```python
# Add caching configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is developed by Batch-26 students of AIMCA for educational purposes.

## 👥 Team

**Batch-26 Students**
- AIMCA (Anjuman Institute of Management & Computer Application)

## 📞 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

## 🔄 Updates & Maintenance

### Regular Maintenance Tasks
1. **Update Dependencies**: `pip install --upgrade -r requirements.txt`
2. **Database Backup**: Regular database backups
3. **Security Updates**: Keep Django and dependencies updated
4. **Performance Monitoring**: Monitor application performance
5. **User Feedback**: Collect and implement user feedback

---

**Last Updated**: July 2025
**Version**: 1.0.0
**Django Version**: 5.2.4
