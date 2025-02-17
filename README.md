# FastAPI User Authentication API

A secure REST API built with FastAPI that provides JWT-based authentication and user management using SQLite database.

## Features

- User registration and authentication
- JWT token-based authentication
- SQLite database integration using SQLAlchemy
- Password hashing with bcrypt
- Protected endpoints
- Interactive API documentation (Swagger UI and ReDoc)

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Install required packages:
```bash
pip install fastapi uvicorn python-jose[cryptography] passlib[bcrypt] python-multipart sqlalchemy