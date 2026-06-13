# 📋 Employee Task Management System

A simple and industry-relevant Task Management System built using Flask and SQLite. This application helps organizations manage employee tasks efficiently through a clean and user-friendly web interface.

## ✨ Features

* ➕ Add new tasks for employees
* 📄 View all assigned tasks
* ✅ Mark tasks as completed
* 🗑️ Delete tasks
* 💾 SQLite database integration
* 🚀 Beginner-friendly Flask application

## 🛠️ Tech Stack

* Python
* Flask
* SQLite
* HTML
* CSS

## 📂 Project Structure

```text
task_manager/
│
├── app.py
├── tasks.db
│
└── templates/
    ├── index.html
    └── add_task.html
```

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/employee-task-manager.git
cd employee-task-manager
```

### Install Dependencies

```bash
pip install flask
```

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 🔄 Workflow

1. Add a new employee task.
2. View all tasks on the dashboard.
3. Mark tasks as completed.
4. Delete tasks when no longer needed.

## 🗄️ Database Schema

| Field    | Type                  |
| -------- | --------------------- |
| id       | Integer (Primary Key) |
| employee | Text                  |
| task     | Text                  |
| status   | Text                  |

## 🚀 Future Enhancements

* 🔐 User Authentication
* 👨‍💼 Admin Dashboard
* 📅 Due Dates
* 🔔 Email Notifications
* 🔍 Search & Filter
* 📊 Analytics Dashboard

## 🎯 Learning Outcomes

* Flask Routing
* CRUD Operations
* SQLite Database Integration
* Template Rendering
* Form Handling
* Web Application Development

## 👨‍💻 Author

**Atharva Gosavi**

⭐ Star this repository if you found it useful!
