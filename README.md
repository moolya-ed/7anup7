Todo App (Full Stack Project)
This is a simple full-stack Todo App built using:

Backend: FastAPI (Python)
Frontend: HTML, CSS, JavaScript
Data Storage: JSON file (`todos.json`)



Project Structure

project-folder/
│
├── app.py                  # FastAPI backend
├── todos.json              # JSON file storing todos
├── functions.py            # Helper functions for todos
├── static/
│   └── index.html          # Frontend code
├── data/
│   └── todos.json          # Used by functions.py (optional)
└── README.md               # This file

 How to Run

### 1. Install Required Packages

Make sure you have Python installed, then run:

```bash
pip install fastapi uvicorn
````

### 2. Start the Backend

Run this command:

```bash
uvicorn app:app --reload
```

This will start the server at:

```
http://127.0.0.1:8000
```

You can open the frontend at:

```
http://127.0.0.1:8000/static/index.html
```

---

## ✏️ Features

* ✅ Add a new todo (title, description)
* 📋 View all todos
* ✏️ Edit a todo (update title, description, status)
* ❌ Delete a todo
* 🔄 Save all changes to `todos.json`

---

## 📂 File Descriptions

* `app.py`: Main FastAPI app with all routes (`/todos`, `/todos/{id}`, etc.)
* `functions.py`: Functions for reading, updating, deleting todos from file
* `todos.json`: Stores the todo data
* `index.html`: Frontend interface (HTML, CSS, JavaScript)

---

## ✅ API Endpoints

| Method | Endpoint      | Description        |
| ------ | ------------- | ------------------ |
| GET    | `/todos`      | Get all todos      |
| POST   | `/todos`      | Add new todo       |
| GET    | `/todos/{id}` | Get one todo by ID |
| PUT    | `/todos/{id}` | Update todo by ID  |
| DELETE | `/todos/{id}` | Delete todo by ID  |

---

## 📌 Note

* The app saves todos in a local file named `todos.json`.
* If the file doesn't exist, it will be created automatically.
* The frontend and backend must run together for full functionality.

---

##  Author

Built by Anup @ Moolya as a learning project.


```

