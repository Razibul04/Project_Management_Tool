#!/usr/bin/env python3
"""
Create a working test user
"""
import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from sqlalchemy import create_engine, text
from app.config import settings

def create_working_user():
    """Create a working test user."""
    try:
        # Create engine
        engine = create_engine(settings.database_url)
        
        with engine.connect() as conn:
            # Drop and recreate users table
            conn.execute(text("DROP TABLE IF EXISTS users"))
            conn.execute(text("""
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    hashed_password VARCHAR(255) NOT NULL,
                    role VARCHAR(20) NOT NULL DEFAULT 'developer',
                    is_active BOOLEAN DEFAULT TRUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """))
            
            # Create test user with simple password hash (password: admin123)
            # This is a bcrypt hash for "admin123"
            simple_hash = "$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4J/8Kz8Kz2"
            
            conn.execute(text("""
                INSERT INTO users (name, email, hashed_password, role)
                VALUES ('Admin User', 'admin@test.com', :password_hash, 'admin')
            """), {"password_hash": simple_hash})
            
            conn.commit()
            
        print("✅ Working test user created successfully!")
        print("Email: admin@test.com")
        print("Password: admin123")
        print("Role: Admin")
        
    except Exception as e:
        print(f"❌ Error creating test user: {e}")

if __name__ == "__main__":
    create_working_user()
