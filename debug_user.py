#!/usr/bin/env python3
"""
Debug the user in database
"""
import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from sqlalchemy import create_engine, text
from app.config import settings
from app.utils.security import verify_password

def debug_user():
    """Debug the user in database."""
    try:
        # Create engine
        engine = create_engine(settings.database_url)
        
        with engine.connect() as conn:
            # Check what's in the database
            result = conn.execute(text("SELECT * FROM users WHERE email = 'admin@test.com'"))
            user = result.fetchone()
            
            if user:
                print("✅ User found in database:")
                print(f"ID: {user[0]}")
                print(f"Name: {user[1]}")
                print(f"Email: {user[2]}")
                print(f"Password Hash: {user[3]}")
                print(f"Role: {user[4]}")
                
                # Test password verification
                test_password = "admin123"
                is_valid = verify_password(test_password, user[3])
                print(f"Password 'admin123' is valid: {is_valid}")
                
                # Try with a new hash
                from app.utils.security import get_password_hash
                new_hash = get_password_hash("admin123")
                print(f"New hash for 'admin123': {new_hash}")
                
                # Update with new hash
                conn.execute(text("""
                    UPDATE users 
                    SET hashed_password = :password_hash 
                    WHERE email = 'admin@test.com'
                """), {"password_hash": new_hash})
                conn.commit()
                
                print("✅ Updated user with new password hash")
                
            else:
                print("❌ No user found in database")
                
    except Exception as e:
        print(f"❌ Error debugging user: {e}")

if __name__ == "__main__":
    debug_user()
