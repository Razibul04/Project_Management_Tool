#!/usr/bin/env python3
"""
Fix the test user password hash
"""
import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from sqlalchemy import create_engine, text
from app.config import settings
from app.utils.security import get_password_hash

def fix_test_user():
    """Fix the test user password hash."""
    try:
        # Create engine
        engine = create_engine(settings.database_url)
        
        with engine.connect() as conn:
            # Get the correct password hash for "admin123"
            correct_hash = get_password_hash("admin123")
            print(f"Correct hash for 'admin123': {correct_hash}")
            
            # Update the user with the correct hash
            result = conn.execute(text("""
                UPDATE users 
                SET hashed_password = :password_hash 
                WHERE email = 'admin@test.com'
            """), {"password_hash": correct_hash})
            
            conn.commit()
            
            if result.rowcount > 0:
                print("✅ Test user password updated successfully!")
                print("Email: admin@test.com")
                print("Password: admin123")
            else:
                print("❌ No user found to update")
                
    except Exception as e:
        print(f"❌ Error updating test user: {e}")

if __name__ == "__main__":
    fix_test_user()
