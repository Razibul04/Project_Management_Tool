#!/usr/bin/env python3
"""
Script to create a test user for the Project Management Tool
"""
import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from app.database import SessionLocal, engine, Base
from app.models.user import User, UserRole
from app.utils.security import get_password_hash

def create_test_user():
    """Create a test user for login."""
    # Create database tables
    Base.metadata.create_all(bind=engine)
    
    # Create database session
    db = SessionLocal()
    
    try:
        # Check if test user already exists
        existing_user = db.query(User).filter(User.email == "admin@test.com").first()
        if existing_user:
            print("✅ Test user already exists!")
            print(f"Email: admin@test.com")
            print(f"Password: admin123")
            return
        
        # Create test user
        hashed_password = get_password_hash("admin123")
        test_user = User(
            name="Admin User",
            email="admin@test.com",
            hashed_password=hashed_password,
            role=UserRole.ADMIN
        )
        
        db.add(test_user)
        db.commit()
        db.refresh(test_user)
        
        print("✅ Test user created successfully!")
        print(f"Email: admin@test.com")
        print(f"Password: admin123")
        print(f"Role: Admin")
        
    except Exception as e:
        print(f"❌ Error creating test user: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_test_user()
