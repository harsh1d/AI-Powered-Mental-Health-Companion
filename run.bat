@echo off
REM MindCompanion Startup Script for Windows

echo.
echo ========================================
echo   🧠 MindCompanion - Mental Health AI
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8+ from python.org
    pause
    exit /b 1
)

echo ✓ Python found
echo.

REM Check if requirements are installed
echo Checking dependencies...
python -c "import streamlit, transformers, torch, nltk, pandas, altair" >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Some dependencies are missing. Installing...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ Failed to install dependencies
        pause
        exit /b 1
    )
)

echo ✓ All dependencies installed
echo.

REM Run component tests
echo Running component tests...
python test_components.py
if errorlevel 1 (
    echo ❌ Component tests failed
    pause
    exit /b 1
)

echo.
echo ========================================
echo   🚀 Starting MindCompanion...
echo ========================================
echo.
echo The app will open in your browser at:
echo 💻 http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.

REM Launch Streamlit
streamlit run app.py

pause
