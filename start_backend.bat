@echo off
echo Starting Backend Server...
cd backend
call venv\Scripts\activate.bat
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --app-dir .
pause
