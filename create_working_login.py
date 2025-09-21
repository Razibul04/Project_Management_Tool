#!/usr/bin/env python3
"""
Create a working login user
"""
import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from sqlalchemy import create_engine, text
from app.config import settings

def create_working_login():
    """Create a working login user."""
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
            
            # Create test user with plain text password for testing
            conn.execute(text("""
                INSERT INTO users (name, email, hashed_password, role)
                VALUES ('Test User', 'test@test.com', 'test123', 'admin')
            """))
            
            conn.commit()
            
        print("✅ Working test user created!")
        print("Email: test@test.com")
        print("Password: test123")
        print("Role: Admin")
        print("")
        print("🎉 You can now login with these credentials!")
        
    except Exception as e:
        print(f"❌ Error creating test user: {e}")

if __name__ == "__main__":
    create_working_login()
