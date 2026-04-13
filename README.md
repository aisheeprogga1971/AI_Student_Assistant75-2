# AI_Student_Assistant75-2
Capstone Project

An AI-powered full-stack Student Assistant web application built using **FastAPI (backend)**, **MongoDB (database)**, and **HTML/CSS/JavaScript (frontend)**.  

This system allows students to:
- Register and login securely
- Ask questions to an AI assistant
- Get instant responses
- Maintain session using browser storage

---

##  Features

### Authentication System
- User Registration
- User Login
- Logout functionality
- Session stored using `localStorage`

### AI Assistant
- Ask any question
- Get instant AI-style responses (backend logic-based)
- Easy to upgrade to real AI (OpenAI / LLMs)

### Database
- MongoDB used for storing users
- Persistent user data
- No data loss after restart

### Frontend
- Simple interactive UI
- JavaScript-based API communication
- Real-time responses
- Login state management

---

## Tech Stack

### Backend
- FastAPI
- Pydantic
- Uvicorn
- PyMongo

### Database
- MongoDB

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)


## Setup

**Backend setup**
pip install fastapi uvicorn pymongo

uvicorn main:app --reload

**Frontend**
Open frontend/index.html using:

✔ Live Server (recommended)
OR
✔ http://localhost:5500

**Finally**
Ask question to test
