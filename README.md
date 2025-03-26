"""
# 🎴 Card Game Web App (Group 6)

This project is a Flask-based web app for playing online card games like Snap and Blackjack. It includes a RESTful API to manage game modes, uses the Deck of Cards API for game logic, and has admin-only protected routes.

---

## 🧩 Technologies
- Python + Flask
- Flask-RESTful (API)
- Flask-SQLAlchemy (Database)
- Deck of Cards API (https://deckofcardsapi.com/)

---

## 🛠️ Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

---

## 🌐 API Endpoints

### Game CRUD (Admin routes require Admin-Key header)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /api/games              | Get all games played (admin) |
| POST   | /api/games              | Add a new finished game |
| PUT    | /api/games/<game_id>   | Update game record (admin) |
| DELETE | /api/games/<game_id>   | Delete game record (admin) |

**Header for Admin routes:**
```http
Admin-Key: your_secret_admin_key
```

### Deck of Cards API Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /api/deck/new                | Create a new shuffled deck |
| GET    | /api/deck/<deck_id>/draw     | Draw cards from a deck |
| GET    | /api/deck/<deck_id>/shuffle  | Shuffle an existing deck |

---

## 🔐 Admin Auth
- `adminauth.py` uses a simple header-based check for admin access.
- Protects POST, PUT, DELETE endpoints on /api/games.

---

## 🧪 Testing
```bash
python test_api.py
```

---

## 🧭 Future Add-ons (Optional Polish)
- Swagger/OpenAPI docs with Flask-RESTX or flasgger
- Advanced user authentication
- Admin dashboard with metrics

---

## 👥 Group Members
- Sophina 
- Liz 
- Sadie 
- Sarah 
- Catriona 
