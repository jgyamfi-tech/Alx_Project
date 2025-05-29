# 📚 Classroom Management App

A full-stack web application for managing classroom activities, tracking student performance, and generating reports. This system includes a **Django REST Framework** backend and a **Vue.js (or React)** frontend.

---

## 🧩 Project Overview

- **Backend:** Django, Django REST Framework, JWT Auth
- **Frontend:** Vue.js or React.js
- **Database:** SQLite (dev) / PostgreSQL (prod)
- **Deployment:** Render, Railway, or AWS

---

## 📦 Features

### 🔒 Authentication
- Register/Login (JWT)
- Role-based access: Admin, Teacher, Student

### 👩‍🏫 Teacher Features
- Add/Edit/Delete student records
- Record scores for exercises, tests, exams
- View performance trends
- Generate analytics reports

### 👨‍🎓 Student Features (Optional)
- View personal performance report

### 🛠 Admin Features
- Manage all users
- Oversee system data and access

---

## 🗂️ Project Structure

```
classroom-management-app/
├── backend/                   # Django REST API
│   ├── api/
│   ├── classroom_management/
│   ├── manage.py
│   ├── requirements.txt
├── frontend/                  # Vue.js or React frontend
│   ├── public/
│   ├── src/
│   ├── package.json
└── README.md
```

---

## 🔧 Backend Setup (Django)

1. Clone the project and navigate to `backend/`

```bash
cd backend
```

2. Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations and start server:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

5. Create a superuser (for admin access):

```bash
python manage.py createsuperuser
```

---

## 🔐 Backend API Overview

### Auth Endpoints

| Method | Endpoint               | Description           |
|--------|------------------------|-----------------------|
| POST   | `/api/auth/register/`  | Register a teacher    |
| POST   | `/api/auth/login/`     | Login & obtain tokens |
| POST   | `/api/auth/refresh/`   | Refresh access token  |

### Teacher Endpoints

| Method | Endpoint                           | Description                |
|--------|------------------------------------|----------------------------|
| GET    | `/api/students/`                   | List students              |
| POST   | `/api/students/`                   | Add student                |
| PUT    | `/api/students/{id}/`              | Update student info        |
| DELETE | `/api/students/{id}/`              | Delete student             |
| POST   | `/api/assessments/`                | Record assessment scores   |
| GET    | `/api/assessments/{student_id}/`   | View student performance   |
| GET    | `/api/performance/`                | Class performance overview |

---

## 🌐 Frontend Setup (Vue.js or React)

1. Navigate to `frontend/`

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start development server:

```bash
npm run dev  # For Vite
# OR
npm start    # For CRA
```

4. Make sure to configure API base URL in `.env`:

```
VITE_API_BASE_URL=http://localhost:8000/api
```

---

## 📊 Visualizations

- Performance charts (Chart.js)
- Weekly/Monthly trends
- Custom dashboards (optional)

---

## 🚀 Deployment Notes

- Use PostgreSQL for production
- Configure CORS and CSRF settings in Django
- Use `.env` for secret management
- Frontend can be deployed via Netlify or Vercel
- Backend via Render or Railway

---

## 📌 Future Enhancements

- Attendance module
- CSV Import/Export
- Notification system
- Multi-classroom and subjects support

---

## 🧪 Testing

- Use Postman or Insomnia for backend API
- Unit tests with Django’s test framework
- End-to-end testing with Cypress or Playwright (Frontend)

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or pull request for any improvements or bug fixes.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 📧 Contact

Built by [Joseph](mailto:gyamfijoseph65@gmail.com) – feel free to reach out!
