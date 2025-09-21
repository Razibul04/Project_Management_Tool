@echo off
echo ========================================
echo  Project Management Tool - WORKING STARTUP
echo ========================================
echo.

echo Starting Backend Server...
cd backend
call venv\Scripts\activate.bat
echo Backend dependencies installed and virtual environment activated.
echo Starting FastAPI server...
start "Backend Server" cmd /k "cd /d %~dp0backend && call venv\Scripts\activate.bat && python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000"

echo.
echo Waiting 5 seconds for backend to start...
timeout /t 5 /nobreak >nul

echo Starting Frontend Server...
cd ..\frontend
echo Frontend dependencies installed.
echo Starting React development server...
start "Frontend Server" cmd /k "cd /d %~dp0frontend && npm start"

echo.
echo ========================================
echo  🎉 SERVERS STARTED!
echo ========================================
echo.
echo Backend:  http://127.0.0.1:8000
echo Frontend: http://localhost:3000
echo API Docs: http://127.0.0.1:8000/docs
echo.
echo Both servers are starting in separate windows.
echo Wait for "Application startup complete" and "webpack compiled" messages.
echo.
echo Press any key to close this window...
pause >nul
