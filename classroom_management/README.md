# 📚 Classroom Management App – Backend

A Django-based RESTful API for managing classroom activities, tracking student performance, and generating progress reports. This backend system enables teachers to record assessments, view performance trends, and manage student data efficiently.

---

## 🚀 Features

- ✅ JWT Authentication (Login & Register)
- 👨‍🏫 Teacher Role: Manage students, record scores, view performance
- 👨‍🎓 Student Role: (Optional) View personal reports
- 🧮 Performance analytics using Pandas/Numpy
- 📊 Integration-ready for frontend chart visualization (Chart.js)
- 🔐 Admin control for managing users and system data

---

## 📦 Tech Stack

- **Backend Framework:** Django, Django REST Framework
- **Authentication:** Simple JWT
- **Data Analysis:** Pandas, Numpy
- **Optional Media Storage:** Cloudinary or AWS S3
- **Database:** SQLite (Dev) / PostgreSQL (Prod)
- **Deployment:** Render / Railway / AWS

---

## 🗂️ Project Structure

```
classroom_management/
├── api/                      # Core app with models, views, serializers
│   ├── migrations/
│   ├── models.py             # CustomUser, Student, Classroom, Assessment
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── classroom_management/     # Project config
│   ├── settings.py
│   ├── urls.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation & Setup

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/classroom-management-backend.git
cd classroom-management-backend
```

2. **Create a Virtual Environment**

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create Superuser (for admin access)**

```bash
python manage.py createsuperuser
```

6. **Run the Server**

```bash
python manage.py runserver
```

---

## 🔐 Authentication

Uses **JWT (JSON Web Tokens)** for secure login and access.

### Auth Endpoints

| Method | Endpoint            | Description           |
|--------|---------------------|-----------------------|
| POST   | `/api/auth/register/` | Register a teacher   |
| POST   | `/api/auth/login/`    | Obtain JWT token     |
| POST   | `/api/auth/refresh/`  | Refresh access token |

---

## 📊 API Endpoints Overview

### 👨‍🏫 Teacher Endpoints

| Method | Endpoint                     | Description                  |
|--------|------------------------------|------------------------------|
| GET    | `/api/students/`             | List all students            |
| POST   | `/api/students/`             | Add a new student            |
| PUT    | `/api/students/{id}/`        | Edit student details         |
| DELETE | `/api/students/{id}/`        | Remove student               |
| POST   | `/api/assessments/`          | Record student scores        |
| GET    | `/api/assessments/{student_id}/` | View student performance |
| GET    | `/api/performance/`          | Get class performance data   |

---

## 🧪 Testing the API

Use [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/) to test endpoints:

1. Register and login to get JWT token
2. Use `Authorization: Bearer <token>` for protected routes

---

## 📤 Deployment

You can deploy this app using:

- [Render](https://render.com/)
- [Railway](https://railway.app/)
- [Heroku](https://heroku.com/) *(deprecated free tier)*

Make sure to:

- Set `DEBUG = False`
- Add `ALLOWED_HOSTS`
- Use PostgreSQL in production
- Configure static/media file handling

---

## 📌 Future Improvements

- Attendance tracking
- CSV import/export of scores
- Notifications and reminders
- Enhanced student dashboard
- Role-based permission controls

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 📧 Contact

Built by [Joseph](mailto:gyamfijoseph65@gmail.com) – feel free to reach out for support or collaboration!
