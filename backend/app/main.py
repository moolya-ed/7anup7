from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
import json
import uuid
import os

app = FastAPI()

# Serve frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_index():
    return FileResponse("static/index.html")

# Allow CORS for frontend JS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class Todo(BaseModel):
    id: str
    title: str
    description: str
    doneStatus: bool

class TodoInput(BaseModel):  # for POST and PUT (no ID)
    title: str
    description: str
    doneStatus: bool

# Data file
DATA_FILE = os.path.join(os.path.dirname(__file__), "todos.json")

# Make sure the JSON file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# Helpers
def load_todos() -> List[Todo]:
    with open(DATA_FILE, "r") as f:
        return [Todo(**todo) for todo in json.load(f)]

def save_todos(todos: List[Todo]):
    with open(DATA_FILE, "w") as f:
        json.dump([todo.dict() for todo in todos], f, indent=2)

# Routes
@app.get("/todos", response_model=List[Todo])
def get_all_todos():
    return load_todos()

@app.post("/todos", response_model=Todo)
def add_todo(todo_input: TodoInput):
    todos = load_todos()
    new_todo = Todo(id=str(uuid.uuid4()), **todo_input.dict())
    todos.append(new_todo)
    save_todos(todos)
    return new_todo

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: str):
    todos = load_todos()
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: str, updated: TodoInput):
    todos = load_todos()
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            updated_todo = Todo(id=todo_id, **updated.dict())
            todos[i] = updated_todo
            save_todos(todos)
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    todos = load_todos()
    filtered = [todo for todo in todos if todo.id != todo_id]
    if len(filtered) == len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    save_todos(filtered)
    return {"message": "Todo deleted successfully"}
