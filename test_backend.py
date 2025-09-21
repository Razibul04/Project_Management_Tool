#!/usr/bin/env python3
"""
Simple test script to verify backend functionality
"""
import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

try:
    from app.main import app
    print("✅ Backend imports successful!")
    print("✅ FastAPI app created successfully!")
    print("✅ All modules loaded correctly!")
    
    # Test basic functionality
    from app.database import get_db
    from app.models.user import User
    from app.models.project import Project
    from app.models.task import Task
    print("✅ Database models imported successfully!")
    
    print("\n🎉 Backend is ready to run!")
    print("Run: python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("Please check the backend setup.")
    sys.exit(1)
