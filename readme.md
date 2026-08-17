<div align="center">

# 📝 To-Do

**A clean, lightweight, and offline-capable task manager built with Python, Flask, and SQLite.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![GitHub Stars](https://img.shields.io/github/stars/Jacekarino/to-do?style=for-the-badge&logo=github&color=EAB308)](https://github.com/Jacekarino/to-do/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Jacekarino/to-do?style=for-the-badge&logo=github&color=6366F1)](https://github.com/Jacekarino/to-do/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/Jacekarino/to-do?style=for-the-badge&logo=github&color=EC4899)](https://github.com/Jacekarino/to-do/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-22C55E?style=for-the-badge&logo=github)](https://github.com/Jacekarino/to-do/pulls)
[![License: MIT](https://img.shields.io/badge/License-MIT-3B82F6?style=for-the-badge&logo=open-source-initiative&logoColor=white)](license.txt)

<br />

<p align="center">
  <img src="https://raw.githubusercontent.com/Jacekarino/to-do/main/thumbnail.png" alt="To-Do App Interface Preview" width="720" />
</p>
<br />

</div>

---

## 🌟 Overview

**To-Do** is a responsive web application designed for fast, frictionless task management. Powered by Python with the Flask micro-framework and SQLite, it offers persistent local data storage, multi-criteria sorting, dynamic drag-and-drop task reordering, and clean task archival.

The app stores data locally in a self-contained SQLite database (`todo.db`), ensuring full functionality offline with instant response times and zero cloud dependencies.

---

## ✨ Features

- ➕ **Fast Task Creation** — Add tasks with rich titles and optional multiline descriptions in a flash.
- 🔀 **Dynamic Reordering & Custom Positions** — Seamlessly drag, drop, and rearrange tasks with real-time asynchronous state sync (`/reorder`).
- 🗂️ **Multi-Dimensional Sorting** — Sort your task backlog on the fly:
  - 🔢 Custom Position (Default)
  - 🕒 Date Added (Oldest / Newest)
  - 🔤 Headline Alphabetical (A-Z / Z-A)
  - 📏 Description Length (Shortest / Longest)
- ✅ **Task Completion & Archival** — Check off completed tasks to move them into an organized completed drawer.
- 🗑️ **Bulk & Individual Deletion** — Delete single tasks or clear all archived completed tasks with a single click.
- 💾 **Persistent Offline Storage** — Powered by SQLite and Flask-SQLAlchemy for durable, local-first data persistence across sessions.
- 📱 **Clean Responsive Interface** — Optimized for both desktop displays and mobile touch screens.

---

## 🛠️ Tech Stack

- **Backend Framework:** Python 3.10+, Flask
- **ORM & Database:** Flask-SQLAlchemy, SQLite (`todo.db`)
- **Templating Engine:** Jinja2
- **Frontend & Styling:** Vanilla HTML5, Modern CSS3, JavaScript (Fetch API for asynchronous drag-and-drop reordering)

---

## 💻 Getting Started

### 1. Clone Repository
```bash
git clone https://github.com/Jacekarino/to-do.git
cd to-do
```

### 2. Set Up Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Activate on macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies & Run
```bash
pip install flask flask-sqlalchemy
python app.py
```

The application will start locally at **`http://127.0.0.1:5001`**.

---

## 📂 Project Structure

```text
to-do/
├── instance/             # SQLite database file directory (todo.db)
├── static/               # CSS styles, client-side JS & frontend assets
│   ├── css/
│   └── js/
├── templates/            # Jinja2 HTML templates
│   └── index.html
├── app.py                # Main Flask application & route handlers
├── thumbnail.png         # Interface preview screenshot
├── license.txt           # MIT License documentation
└── readme.md             # Project documentation
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the Project (**Fork**)
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a **Pull Request**

---

## 📄 License

Distributed under the **MIT License**. See [`license.txt`](license.txt) for more information.

---

<div align="center">

Made with ♡ by [**Jacekarino**](https://github.com/Jacekarino)

</div>
