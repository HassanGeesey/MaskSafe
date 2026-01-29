@echo off
echo ========================================
echo   MaskSafe - Starting Application
echo ========================================
echo.

REM Activate conda base environment
call note
echo Starting Flask application...
echo.
echo ========================================
echo   MaskSafe is running!
echo   Open: http://127.0.0.1:5000
echo ========================================
echo.
echo Press Ctrl+C to stop the server
echo.

REM Run the Flask app
python app.py

REM Keep window open after server stops
echo.
echo Server stopped.
pause