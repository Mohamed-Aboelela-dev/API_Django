# Django API Project

This is a Django-based REST API project .

## 📦 Project Structure

```
API_Django/
├── Project/
│   ├── manage.py
│   ├── db.sqlite3
│   └── Project/
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       ├── urls.py
│       └── ...
├── requirements.txt
```

## 🚀 Getting Started

### Requirements

- Python 3.8+
- pip (Python package installer)
- Virtualenv (recommended)

### Installation


1. **Clone this repository:**

   ```bash
   git clone <git@github.com:Mohamed-Aboelela-dev/API_Django.git>
   cd API_Django/Project
   ```


2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  
   ```

3. **Install dependencies:**

   ```bash
   pip install -r ../requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

## 🔌 API Endpoints

*Assuming generic CRUD endpoints for this model (CatFact):*
_________________________________________________________
 GET    | `/catfacts/`        |   List all cat facts    |
 POST   | `/catfacts/`        |   Create a new cat fact |
 GET    | `/catfacts/<id>/`   |   Retrieve a cat fact   |
 PUT    | `/catfacts/<id>/`   |   Update a cat fact     |
 DELETE | `/catfacts/<id>/`   |   Delete a cat fact     |


