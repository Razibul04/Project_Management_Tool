@echo off
echo ========================================
echo  Project Management Tool Setup & Run
echo ========================================
echo.

echo [1/4] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found! Please install Python 3.8+
    pause
    exit /b 1
)
echo ✅ Python found

echo.
echo [2/4] Checking Node.js installation...
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js not found! Please install Node.js
    pause
    exit /b 1
)
echo ✅ Node.js found

echo.
echo [3/4] Setting up Backend...
cd backend
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing Python dependencies...
pip install -r requirements.txt >nul 2>&1

echo Testing backend imports...
cd ..
python test_backend.py
if errorlevel 1 (
    echo ❌ Backend setup failed!
    pause
    exit /b 1
)

echo.
echo [4/4] Setting up Frontend...
cd frontend
if not exist "node_modules" (
    echo Installing Node.js dependencies...
    npm install
)

echo.
echo ========================================
echo  Setup Complete! Starting servers...
echo ========================================
echo.

echo Starting Backend Server...
start "Backend Server" cmd /k "cd backend && call venv\Scripts\activate.bat && python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --app-dir ."

echo Waiting 5 seconds for backend to start...
timeout /t 5 /nobreak >nul

echo Starting Frontend Server...
start "Frontend Server" cmd /k "cd frontend && npm start"

echo.
echo ========================================
echo  🎉 Application Started Successfully!
echo ========================================
echo.
echo Frontend: http://localhost:3000
echo Backend:  http://localhost:8000
echo API Docs: http://localhost:8000/docs
echo.
echo Press any key to close this window...
pause >nul
