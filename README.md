# 🧪 Automated Testing Framework Demo

## 📌 Overview
This project is a **Flask-based web application** that demonstrates automated testing practices for backend APIs.  
It provides a simple **REST API** for managing a list of items and integrates **automated testing** to ensure reliability and maintainability.

The project is designed as a foundation for learning **API development, testing workflows, and future deployment strategies**.

---

## 🛠️ Tech Stack
| Category            | Technology Used          |
|---------------------|-------------------------|
| Backend Framework   | Flask (Python)          |
| Testing Framework   | Pytest                  |
| UI Testing (Planned)| Selenium WebDriver      |
| Version Control     | Git + GitHub            |
| Virtual Environment | venv                    |
| Future Deployment   | Docker / Render / Heroku|

---

## ⚙️ Features Implemented
✅ **Flask REST API** with GET and POST endpoints (`/items`)  
✅ **JSON-based communication** between client and server  
✅ **Unit Tests** to validate individual endpoints  
✅ **Integration Tests** to validate workflows end-to-end  
✅ **Virtual environment setup** for clean dependency management  
✅ Ready for future expansion (UI tests, databases, CI/CD)

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/lulusartajmd/automated-testing-framework-demo.git
cd automated-testing-framework-demo

### 2. Create and Activate Virtual Environment
python -m venv venv
# Activate
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run the App
python app.py

The app will be available at http://127.0.0.1:5000/

| Method | Endpoint | Description               |
| ------ | -------- | ------------------------- |
| GET    | `/items` | Returns list of all items |
| POST   | `/items` | Adds a new item via JSON  |

# Example POST request body:

{ "name": "Apple" }

# Testing

Run automated tests with:

pytest -v

## Tests included:

Unit tests: Validate individual API endpoints.

Integration tests: Validate end-to-end workflows.

## Roadmap

🔹- Add UI testing with Selenium
🔹- Integrate a database (SQLite/PostgreSQL)
🔹- Add authentication & authorization
🔹- Set up CI/CD pipelines (GitHub Actions)
🔹- Containerize app with Docker for deployment
