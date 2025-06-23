 Late Show API
A Flask REST API for managing a Late Night Show's guests, episodes, and appearances, built with PostgreSQL, JWT authentication, and tested via Postman.

 Tech Stack
Python (Flask)

PostgreSQL

SQLAlchemy + Alembic

Flask-Migrate

Flask-JWT-Extended

Pipenv

Postman

 Folder Structure
pgsql
Copy
Edit
.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   │   ├── user.py
│   ├── controllers/
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   ├── auth_controller.py
├── migrations/
├── Pipfile
├── Pipfile.lock
├── challenge-4-lateshow.postman_collection.json
└── README.md
 Setup Instructions
 Install Dependencies
bash
Copy
Edit
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
 Create PostgreSQL Database
sql
Copy
Edit
CREATE DATABASE late_show_db;
 Set Database URI
server/config.py

python
Copy
Edit
SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = "your-secret-key"
 Run Migrations
bash
Copy
Edit
export PYTHONPATH=.
export FLASK_APP=server.app:create_app

flask db init             # only once
flask db migrate -m "initial"
flask db upgrade
Seed the Database
bash
Copy
Edit
python server/seed.py
 Authentication Flow
1. Register
POST /register

json
Copy
Edit
{
  "username": "john123",
  "password": "securepass"
}
2. Login
POST /login

json
Copy
Edit
{
  "username": "john123",
  "password": "securepass"
}
Returns:

json
Copy
Edit
{
  "access_token": "your.jwt.token"
}
Use in header:

makefile
Copy
Edit
Authorization: Bearer <access_token>
📡 Routes & Sample Usage
Endpoint	Method	Auth?	Description
/register	POST	❌	Register user
/login	POST	❌	Login & get token
/episodes	GET	❌	List all episodes
/episodes/<id>	GET	❌	Get one episode with guests
/episodes/<id>	DELETE	✅	Delete episode & appearances
/guests	GET	❌	List all guests
/appearances	POST	✅	Create new appearance

Example: Create Appearance (Requires Auth)
POST /appearances

json
Copy
Edit
{
  "rating": 4,
  "guest_id": 1,
  "episode_id": 2
}
Header:

makefile
Copy
Edit
Authorization: Bearer <access_token>
 Postman Collection
 Import challenge-4-lateshow.postman_collection.json into Postman
Test all endpoints
 Use token in protected routes

 Submission
All models & validations complete

JWT auth implemented

 Seed data works

 All routes tested

 PostgreSQL used

Clean, working MVC

 GitHub repo: [your GitHub repo link here]

