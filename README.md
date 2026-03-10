# URL Shortener

A full-stack **URL Shortener web application** that converts long URLs into short, shareable links and tracks usage statistics. The project demonstrates backend API design, database integration, and frontend-backend communication.

---

## Features

* Convert long URLs into short URLs
* Redirect users from short URL to original URL
* Track number of clicks for each shortened URL
* REST API built with FastAPI
* React frontend for user interaction
* MySQL database for persistent storage

---

## Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* MySQL
* Uvicorn

### Frontend

* React
* Axios
* CSS

---

## Project Structure

```
url_shortener
│
├── backend
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── routes.py
│   └── requirements.txt
│
├── frontend
│   ├── src
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   └── package.json
│
└── README.md
```

---

## How It Works

1. User enters a long URL in the frontend.
2. Frontend sends a request to the backend API.
3. Backend generates a unique short code.
4. Short URL is stored in the database.
5. When the short URL is visited, the backend redirects to the original URL and increments the click count.

---

## API Endpoints

### Create Short URL

```
POST /shorten
```

Request body:

```
{
  "original_url": "https://example.com"
}
```

Response:

```
{
  "short_url": "http://localhost:8000/abc123"
}
```

---

### Redirect to Original URL

```
GET /{short_code}
```

Example:

```
http://localhost:8000/abc123
```

Redirects the user to the original URL.

---

### Get URL Statistics

```
GET /stats/{short_code}
```

Response:

```
{
  "original_url": "https://example.com",
  "clicks": 5
}
```

---

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

---

## Backend Setup

Navigate to the backend folder:

```
cd backend
```

Create virtual environment:

```
python -m venv venv
```

Activate virtual environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the backend server:

```
uvicorn main:app --reload
```

Backend will run on:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

Navigate to frontend folder:

```
cd frontend
```

Install dependencies:

```
npm install
```

Run the frontend:

```
npm start
```

Frontend will run on:

```
http://localhost:3000
```

---

## Database Setup

Create a MySQL database:

```
CREATE DATABASE url_shortener;
```

Update database connection in `database.py`.

Tables will be created automatically when the backend starts.

---

## Example Workflow

1. Enter a long URL in the frontend.
2. Click **Shorten URL**.
3. Application returns a short URL.
4. Visiting the short URL redirects to the original link.
5. Click count is updated in the database.

---

## Future Improvements

* User authentication
* Custom short URLs
* QR code generation
* URL expiration
* Analytics dashboard

---

## License

This project is for educational purposes.
