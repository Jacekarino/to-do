# Allow Windows PowerShell to run scripts:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Build Flask:

.\venv\Scripts\Activate.ps1

# Run project:

python app.py

# Access web app:

localhost:5001

# Stop server:

Ctrl + C