# 🎴 Card Game Web App (Group 6)

This project is a Flask-based web app for playing online card games like Snap and Blackjack. It includes a RESTful API to manage game modes, uses the Deck of Cards API for game logic, and has admin-only protected routes.

---

## 🧩 Technologies
- Python + Flask
- Flask-RESTful (API)
- Flask-SQLAlchemy (Database)
- flasgger (API Docs)
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

### Game CRUD
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /api/games              | Get all games played (admin) |
| POST   | /api/games              | Add a new finished game |
| PUT    | /api/games/<game_id>   | Update game record (admin) |
| DELETE | /api/games/<game_id>   | Delete game record (admin) |

### API Documentation
| Endpoint | Description |
|----------|-------------|
| /apidocs | Returns a swagger UI |

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
- Advanced user authentication
- Additional metrics for the admin app
- Blackjack game mode

---

## 👥 Group Members
- Sophina 
- Liz 
- Sadie 
- Sarah 
- Catriona 
