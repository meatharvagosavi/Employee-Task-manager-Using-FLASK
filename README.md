# Employee Task Management System

A simple and industry-relevant Task Management System built using Flask and SQLite. This application allows organizations to manage employee tasks efficiently through a clean web interface.

## Features

* Add new tasks for employees
* View all assigned tasks
* Mark tasks as completed
* Delete tasks
* SQLite database integration
* Simple and beginner-friendly Flask application

## Tech Stack

* Python
* Flask
* SQLite
* HTML
* CSS

## Project Structure

```text
task_manager/
│
├── app.py
│
└── templates/
    ├── index.html
    └── add_task.html
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/employee-task-manager.git
cd employee-task-manager
```

### Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install flask
```

## Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Application Workflow

1. Add a new employee task.
2. View all tasks on the dashboard.
3. Update task status to Completed.
4. Delete completed or unwanted tasks.

## Database Schema

| Field    | Type                  |
| -------- | --------------------- |
| id       | Integer (Primary Key) |
| employee | Text                  |
| task     | Text                  |
| status   | Text                  |

## Future Enhancements

* User Authentication
* Employee Login System
* Admin Dashboard
* Task Priority Levels
* Due Dates and Notifications
* Search and Filter Functionality
* REST API Integration

## Learning Outcomes

This project demonstrates:

* Flask Routing
* CRUD Operations
* SQLite Database Handling
* Template Rendering
* Form Processing
* Web Application Development Fundamentals

## Author

Atharva Gosavi

---

⭐ If you found this project useful, consider giving it a star on GitHub.
