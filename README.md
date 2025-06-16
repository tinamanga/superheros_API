# superheros_API

A RESTful API built with Flask that models superheroes, their powers, and the strength of their abilities. This was created as part of the Flatiron Phase 4 Code Challenge.

## Description

This application provides a way to manage superheroes and their powers using Flask, SQLAlchemy, and SQLite. It includes proper relationships, validations, and RESTful routes.

## Key Features

- View all heroes and individual hero details.
- View all powers and individual power details.
- Update a power's description.
- Assign a power to a hero with a specific strength (Strong, Weak, or Average).
- Validation for strength choices.
- Error handling with informative JSON responses.

## Technologies Used

- Python 3
- Flask
- Flask SQLAlchemy
- flask migration
- SQLite (as the database)

## Project Structure

.
├── app.py 
├── models.py 
├── routes.py
├── extensions.py 
├── seed.py 
├── migrations/ 
├── instance/app.db 
├── README.md 
└── requirements.txt 

```bash

## Setup Instructions
1. Clone the repository

```bash
git clone https://github.com/yourusername/flask-superheroes-api.git
cd flask-superheroes-api
```
2. Create a virtual environment and activate it

```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies

```bash

   pip install -r requirements.txt
   ```
4. Run migrations and seed the database

```bash

flask db init     # Only needed once
flask db migrate -m "Initial migration"
flask db upgrade
```
5. python seed.py
Start the server

```bash
python app.py
The server will run on http://127.0.0.1:5555.
```
## API Endpoints
- Heroes
    GET /heroes – Returns a list of all heroes

    GET /heroes/<id> – Returns detailed info about one hero (including their powers)

- Powers
   GET /powers – Returns all powers

   GET /powers/<id> – Returns one power

   PATCH /powers/<id> – Updates a power's description

- Hero Powers
    POST /hero_powers – Assigns a power to a hero with a strength (Strong, Weak, Average)

Payload Example:

json
Copy
Edit
{
  "strength": "Strong",
  "power_id": 1,
  "hero_id": 1
}
Success Response:

json
Copy
Edit
{
  "id": 1,
  "name": "Batman",
  "super_name": "Dark Knight",
  "powers": [
    {
      "id": 1,
      "name": "Invisibility",
      "description": "Turns invisible at will"
    }
  ]
}
Validation Error Example:

json
Copy
Edit
{
  "errors": ["Strength must be Strong, Weak, or Average"]
}
⚠️ Validations
HeroPower.strength must be "Strong", "Weak", or "Average"

Power.description must not be null

## Author
Christina Manga
[christinamanga28@gmail.com]

## License
This project is licensed under the MIT License.


