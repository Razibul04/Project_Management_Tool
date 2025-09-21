#!/usr/bin/env python3
"""
Test simple login without password verification
"""
import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from sqlalchemy import create_engine, text
from app.config import settings

def create_simple_user():
    """Create a simple user for testing."""
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
                VALUES ('Admin User', 'admin@test.com', 'admin123', 'admin')
            """))
            
            conn.commit()
            
        print("✅ Simple test user created!")
        print("Email: admin@test.com")
        print("Password: admin123")
        print("Note: Using plain text password for testing")
        
    except Exception as e:
        print(f"❌ Error creating test user: {e}")

if __name__ == "__main__":
    create_simple_user()
