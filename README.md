
#  URL Shortener

A full-stack URL Shortener built using **Flask**, **PostgreSQL**, and **JavaScript**. The application allows users to shorten long URLs, redirect using short links, and track click statistics. It also uses an **LRU Cache** to improve redirect performance.

---

##  Features

-  Shorten long URLs using Base62 encoding
-  Redirect users using short URLs
-  View click statistics for each shortened URL
-  LRU Cache for faster URL lookup
-  PostgreSQL database integration
-  RESTful APIs built with Flask
-  Responsive frontend using HTML, CSS, and JavaScript
-  Copy shortened URL to clipboard
-  Open shortened URL directly from the frontend

---

##  Tech Stack

### Backend
- Python
- Flask
- PostgreSQL
- psycopg2
- Flask-CORS

### Frontend
- HTML5
- CSS3
- JavaScript (Fetch API)

### Concepts Used
- Base62 Encoding
- LRU Cache
- REST APIs
- CRUD Operations

---

#  Project Structure

```text
url-shortener/
│
├── backend/
│   ├── app.py
│   ├── base62.py
│   ├── cache.py
│   ├── config.py
│   ├── db.py
│   ├── requirements.txt
│   └── routes/
│       ├── shorten.py
│       ├── redirect.py
│       └── stats.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
└── README.md
```

---

#  Setup Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/anjini27/url-shortener.git
cd url-shortener
```

---

## 2. Create a Virtual Environment

```bash
cd backend

python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure PostgreSQL

Create a PostgreSQL database:

```sql
CREATE DATABASE url_shortener;
```

Update your database configuration in `config.py`.

---

## 5. Create Database Table

```sql
CREATE TABLE urls (
    id SERIAL PRIMARY KEY,
    original_url TEXT NOT NULL,
    short_code VARCHAR(20) UNIQUE,
    click_count INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

#  Run Backend

```bash
cd backend

source venv/bin/activate

python app.py
```

Backend runs at:

```
http://127.0.0.1:5000
```

---

#  Run Frontend

Open another terminal:

```bash
cd frontend

python3 -m http.server 8000
```

Frontend runs at:

```
http://127.0.0.1:8000
```

---

#  API Endpoints

## 1. Shorten URL

**POST**

```
/api/shorten
```

Request

```json
{
  "url": "https://www.google.com"
}
```

Response

```json
{
  "id": 1,
  "original_url": "https://www.google.com",
  "short_code": "B",
  "short_url": "http://localhost:5000/B"
}
```

---

## 2. Redirect

**GET**

```
/<short_code>
```

Example

```
http://localhost:5000/B
```

Redirects to the original URL.

---

## 3. Statistics

**GET**

```
/api/stats/<short_code>
```

Example

```
/api/stats/B
```

Response

```json
{
  "id": 1,
  "original_url": "https://www.google.com",
  "short_code": "B",
  "click_count": 5,
  "created_at": "2026-07-08T04:08:02"
}
```

---

#  Application Flow

## URL Shortening

```
User
 │
 ▼
Enter Long URL
 │
 ▼
POST /api/shorten
 │
 ▼
Store Original URL
 │
 ▼
Generate ID
 │
 ▼
Base62 Encode
 │
 ▼
Save Short Code
 │
 ▼
Return Short URL
```

## Redirect

```
User
 │
 ▼
GET /<short_code>
 │
 ▼
Check LRU Cache
 │
 ├── Cache Hit
 │
 └── Cache Miss
      │
      ▼
PostgreSQL
      │
      ▼
Increment Click Count
      │
      ▼
Redirect User
```

---

#  Learning Outcomes

Through this project, I learned:

- Flask Backend Development
- PostgreSQL Integration
- REST API Design
- Base62 Encoding Algorithm
- CRUD Operations
- LRU Cache Implementation
- Frontend-Backend Communication
- JavaScript Fetch API
- CORS Configuration
- Full-Stack Project Structure

---

#  Future Improvements

- QR Code Generation
- URL Validation
- Duplicate URL Detection
- Docker Support
- Docker Compose
- Custom Short URLs
- User Authentication
- URL Expiration
- Cloud Deployment

---

#  Author

**Bhukya Anjini**

- GitHub: https://github.com/anjini27

---

## ⭐ If you found this project useful, please consider giving it a star!
