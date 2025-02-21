from sqlalchemy import Column, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base
from datetime import datetime  # Changed import

# Database Model
class UserDB(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    disabled = Column(Boolean, default=False)
    hashed_password = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=datetime.now())  # Fixed datetime.now() call