#!/usr/bin/env python3
"""
Simple script to create a test user
"""
import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from sqlalchemy import create_engine, text
from app.config import settings

def create_test_user():
    """Create a test user directly in the database."""
    try:
        # Create engine
        engine = create_engine(settings.database_url)
        
        # Create tables first
        with engine.connect() as conn:
            # Create users table if it doesn't exist
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS users (
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
            
            # Check if test user exists
            result = conn.execute(text("SELECT id FROM users WHERE email = 'admin@test.com'"))
            if result.fetchone():
                print("✅ Test user already exists!")
                print("Email: admin@test.com")
                print("Password: admin123")
                return
            
            # Create test user (password: admin123)
            conn.execute(text("""
                INSERT INTO users (name, email, hashed_password, role)
                VALUES ('Admin User', 'admin@test.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4J/8Kz8Kz2', 'admin')
            """))
            
            conn.commit()
            
        print("✅ Test user created successfully!")
        print("Email: admin@test.com")
        print("Password: admin123")
        print("Role: Admin")
        
    except Exception as e:
        print(f"❌ Error creating test user: {e}")

if __name__ == "__main__":
    create_test_user()
