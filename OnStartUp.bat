@ECHO OFF
PowerShell -Command "Set-ExecutionPolicy Unrestricted -Scope Process"
cd /d "%~dp0"
call .venv\Scripts\activate