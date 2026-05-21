# Allow Windows PowerShell to run scripts:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Build Flask:

.\venv\Scripts\Activate.ps1

# Run project:

python app.py

# Access website:

http://127.0.0.1:5001

# Stop server:

Ctrl + C