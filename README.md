# 💰 Finance Dashboard Backend API

A role-based backend system for managing financial records with secure access control, built using **Django**, **Django REST Framework**, and **JWT Authentication**.

---

## 🌐 Live API

Base URL:
https://finance-dashboard-lilb.onrender.com/api/

> Note: Since the API is secured, please create a user via `/api/users/` (first user allowed without authentication) and obtain a JWT token using `/api/token/` before accessing other endpoints. All endpoints require JWT authentication.

---

## 🧪 How to Test (Live API)

1. Create a user (if none exists):

POST /api/users/

{
  "username": "admin",
  "password": "admin123",
  "role": "admin"
}

2. Get JWT Token:

POST /api/token/

3. Use token in header:

Authorization: Bearer <access_token>

4. Access endpoints:

/api/users/
/api/records/
/api/summary/

---

## 🚀 Features

* 🔐 JWT Authentication (Login with token)
* 👤 Role-Based Access Control

  * **Admin** → Full access (CRUD + manage users + global summary)
  * **Analyst** → Create & view own records
  * **Viewer** → Read-only access
* 💰 Financial Records Management

  * Create, Read, Update, Delete
* 📊 Dashboard Summary

  * Total Income
  * Total Expense
  * Net Balance
* 🔍 Filtering Support

  * By **type** (income/expense)
  * By **category**
  * By **date**
* 👥 User-specific Data Isolation
* ⚡ Admin can create records for any user

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite
* JWT (SimpleJWT)

---

## 📁 Project Structure

finance_dashboard/
│
├── api/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── urls.py
│
├── finance_dashboard/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
├── .env (not included in repo)

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/Slayezs/Finance-dashboard-backend.git
cd finance-dashboard
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your-secret-key
```

---

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

---

### 7. Run Server

```bash
python manage.py runserver
```

---

## 🔐 Authentication

### Get Token

```http
POST /api/token/
```

```json
{
  "username": "admin",
  "password": "password"
}
```

---

### Use Token

Add header:

```http
Authorization: Bearer <access_token>
```

---

## 📌 API Endpoints

### 👤 Users

| Method | Endpoint    | Description              |
| ------ | ----------- | ------------------------ |
| POST   | /api/users/ | Create user (Admin only) |
| GET    | /api/users/ | List users               |

---

### 💰 Financial Records

| Method | Endpoint           | Description   |
| ------ | ------------------ | ------------- |
| POST   | /api/records/      | Create record |
| GET    | /api/records/      | List records  |
| PUT    | /api/records/{id}/ | Update        |
| DELETE | /api/records/{id}/ | Delete        |

---

### 📊 Dashboard Summary

```http
GET /api/summary/
```

---

### Sample Summary Response

{
  "total_income": 10000,
  "total_expense": 5000,
  "net_balance": 5000
}

---
## 🔍 Filtering Examples

```http
GET /api/records/?type=income
GET /api/records/?category=Food
GET /api/records/?date=2026-04-01
GET /api/records/?type=expense&category=Food
```

---

## 🧠 Role-Based Access Logic

| Role    | Permissions                              |
| ------- | ---------------------------------------- |
| Admin   | Full CRUD + Manage users + View all data |
| Analyst | Create & view own records                |
| Viewer  | Read-only access                         |

---

## 🔒 Security

* Secret key stored in `.env`
* `.env` excluded via `.gitignore`
* JWT authentication for all protected APIs

---

## 📈 Future Improvements

* Pagination
* Search functionality
* Deployment (Render / AWS)
* API documentation (Swagger)

---

## ⭐ Conclusion

This project demonstrates backend development skills including API design, authentication, role-based access control, and data handling in a real-world scenario.

---
