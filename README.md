# 💼 Job Portal System (FastAPI)

This project is a **backend system for a Job Portal** built with **FastAPI**. It provides job listings, user management, and CRUD operations for job postings.

It is an **API-first backend** project, designed purely for backend functionality with no frontend or bot integration.

---

## ✨ Key Features

* **Job Management:** Create, update, delete, and list job postings.
* **User Management:** Register and manage users.
* **Database Handling:** Uses SQLite for storing job and user data.
* **Async Operations:** Asynchronous database queries for performance.
* **API Documentation:** Automatic OpenAPI/Swagger docs.

---

## 🔹 Project Structure

```
Job-Portal-System-FastAPI/
├── api/                  # API endpoints for jobs and users
│   ├── endpoints.py
│   ├── services.py
│   └── models.py
├── database/             # Database connection and models
│   └── database.py
├── main.py               # FastAPI app entry point
├── requirements.txt      # Python dependencies
└── README.md
```

---

## 🛠 Tech Stack

* **Python 3.10+**
* **FastAPI**
* **SQLite**
* **SQLAlchemy / Tortoise ORM** (for async DB handling)
* **Pydantic** (data validation)
* **Git / GitHub**

---

## 👤 User Flow

1. Users register and manage their accounts.
2. Users can view job listings.
3. Admins can create, update, or delete job postings.
4. All CRUD operations are handled asynchronously.
5. API endpoints are documented via `/docs` or `/redoc`.

---

## 🔑 Environment Variables (.env)

```
DEBUG=True
DATABASE_URL=sqlite:///job_portal_system.db
SECRET_KEY=your_secret_key
```

---

## 📄 License

Private project, intended for learning and personal portfolio.

---

## 👨‍💻 Author

Developed by **Muhammadumar Umarov**
Telegram: @Muhammadumar_umarov
Python Developer
