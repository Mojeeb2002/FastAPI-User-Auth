# FastAPI User Authentication API

A secure REST API built with FastAPI that provides JWT-based authentication and user management using SQLite database.

## Features

- User registration and authentication
- JWT token-based authentication
- SQLite database integration using SQLAlchemy
- Password hashing with bcrypt
- Protected endpoints
- Interactive API documentation (Swagger UI and ReDoc)
- Session management with SQLAlchemy
- Custom user models and schemas

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Dependencies

```bash
fastapi==0.68.1
uvicorn==0.15.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.5
sqlalchemy==1.4.23
```

## Installation

1. Install required packages:
```bash
pip install fastapi uvicorn python-jose[cryptography] passlib[bcrypt] python-multipart sqlalchemy