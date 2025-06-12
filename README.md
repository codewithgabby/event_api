# README.md
# Event Management API System

This is a FastAPI exam project that allows users to register for events, track attendance, and manage both event and speaker information.

> I really enjoyed working on this. It was a bit challenging to get the registration validation right, but I learned a lot.

---

## How to Run the Project

1. **Clone the repository**  
```bash
git clone git@github.com:codewithgabby/event_api.git
cd event_api


Create a virtual environment:

python -m venv venv
venv\Scripts\activate   # I use Windows


Install FastAPI and Uvicorn:

pip install fastapi uvicorn


Run the application:

uvicorn main:app --reload


Test the endpoints
Open your browser and go to:
http://127.0.0.1:8000/docs


Tech Stack:

# Python

# FastAPI

# Pydantic

# Uvicorn

# In-memory storage (lists)


> Note: You can test duplicate registration prevention by trying to register the same user twice for the same event. The API will return an error if the user is already registered.









