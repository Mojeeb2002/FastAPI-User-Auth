from sqlalchemy import Column, String, Boolean
from .database import Base

# Database Model
class UserDB(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, index=True)
    email = Column(String)
    full_name = Column(String)
    disabled = Column(Boolean, default=False)
    hashed_password = Column(String)