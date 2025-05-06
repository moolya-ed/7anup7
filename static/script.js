const API_URL = "http://127.0.0.1:8000/todos";

// Load todos
async function fetchTodos() {
  const res = await fetch(API_URL);
  const todos = await res.json();
  const todoList = document.getElementById("todo-list");
  todoList.innerHTML = "";

  todos.forEach(todo => {
    const li = document.createElement("li");
    li.innerHTML = `
      <strong>${todo.title}</strong><br>
      ${todo.description}<br>
      Status: ${todo.doneStatus ? "Done" : "Not Done"}<br>
      <button onclick="editTodo('${todo.id}')">Edit</button>
      <button onclick="deleteTodo('${todo.id}')">Delete</button>
    `;
    todoList.appendChild(li);
  });
}

// Add a new todo
async function addTodo() {
  const title = document.getElementById("title").value;
  const description = document.getElementById("description").value;
  const doneStatus = false; // Default value for a new todo
  
  const todo = { title, description, doneStatus };

  const res = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(todo),
  });

  fetchTodos(); // Refresh the todo list
}

// Update a todo
async function updateTodo() {
  const id = document.getElementById("update-id").value;
  const title = document.getElementById("update-title").value;
  const description = document.getElementById("update-description").value;
  const doneStatus = document.getElementById("update-completed").checked;

  const updatedTodo = { title, description, doneStatus };

  const res = await fetch(`${API_URL}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(updatedTodo),
  });

  fetchTodos(); // Refresh the todo list
}

// Delete a todo
async function deleteTodo() {
  const id = document.getElementById("delete-id").value;

  await fetch(`${API_URL}/${id}`, {
    method: "DELETE",
  });

  fetchTodos(); // Refresh the todo list
}

// Edit todo
async function editTodo(id) {
  const todo = await fetch(`${API_URL}/${id}`).then(res => res.json());
  
  document.getElementById("update-id").value = todo.id;
  document.getElementById("update-title").value = todo.title;
  document.getElementById("update-description").value = todo.description;
  document.getElementById("update-completed").checked = todo.doneStatus;
}
