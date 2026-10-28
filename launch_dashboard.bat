@echo off
cd /d "%~dp0"
start "" "C:\Users\rahul\AppData\Local\Programs\Python\Python314\pythonw.exe" "%~dp0serve.py"
timeout /t 1 /nobreak >nul
start "" http://localhost:8080
exit
