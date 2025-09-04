# Automated Testing Framework Demo

## Description
This is a small Flask web app that demonstrates automated testing concepts. 
Users can add items and retrieve them via API endpoints.

## Technologies Used
- Python
- Flask
- Pytest
- Selenium

## Setup
1. Clone the repo
2. Create a virtual environment: `python -m venv venv`
3. Activate venv: 
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `python app.py`

## API Endpoints
- `GET /items` → returns list of items
- `POST /items` → add a new item by sending JSON `{ "name": "item name" }`

## Testing
- Unit and integration tests using `pytest`
- UI tests using Selenium

## Future Improvements
- Connect to a real database
- Add authentication
- Add more API routes
