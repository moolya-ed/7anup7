import os
import json
import logging
import uuid
from pydantic import BaseModel
from typing import Optional

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load todos from the JSON file
def load_list():
    file_path = "data/todos.json"
    if not os.path.exists(file_path):
        logging.warning("File not found. Returning empty list.")
        return []

    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        return []

# Save todos to the JSON file
def save_list(todo_list):
    try:
        os.makedirs("data", exist_ok=True)  # Ensure directory exists
        with open("data/todos.json", "w") as file:
            json.dump(todo_list, file, indent=2)
    except Exception as e:
        logging.error(f"Error writing to file: {e}")
        # Debugging: Check the correct path of the file
print(f"Saving todos to: {DATA_FILE}")


# Get a specific todo by its ID
def get_todo_details(todo_id):
    todos = load_list()
    for todo in todos:
        if todo.get("id") == todo_id:
            return todo
    logging.error(f"Todo with id {todo_id} not found.")
    return None  # Instead of raising an exception, return None

# Remove a todo by its ID
def remove_todo(todo_id):
    todos = load_list()
    updated_todos = []
    found = False

    for todo in todos:
        if todo.get("id") == todo_id:
            found = True
        else:
            updated_todos.append(todo)

    if not found:
        logging.error(f"Todo with id {todo_id} not found.")
        return None  # Return None if the todo is not found

    save_list(updated_todos)
    logging.info(f"Todo with id {todo_id} has been removed.")
    return todo_id  # Return the ID of the deleted todo

# Update a todo by its ID
def update_todo(todo_id, new_data):
    todos = load_list()
    found = False

    for todo in todos:
        if todo.get("id") == todo_id:
            for key in new_data:
                if key in todo:
                    todo[key] = new_data[key]
            found = True
            break

    if not found:
        logging.error(f"Todo with id {todo_id} not found.")
        return None  # Return None if the todo is not found

    save_list(todos)
    logging.info(f"Todo with id {todo_id} has been updated.")
    return todo_id  # Return the ID of the updated todo

# Generate a new unique ID
def generate_id():
    return uuid.uuid4().hex

# Test the functions
def try_get_todo_by_id(todo_id):
    todo = get_todo_details(todo_id)
    if todo:
        print(f"Found Todo: {todo}")
    else:
        print(f"Todo with ID {todo_id} not found.")

if __name__ == "__main__":
    print("All Todos:")
    todos = load_list()
    print(todos)  # Load and print all todos

    print("\nGenerate New ID:")
    print(generate_id())  # Print a newly generated ID

    print("\nTry to Get Todo by ID:")
    todo_id_to_test = "8af52e54045b423aabaa9bcf7003ff4d"  # Replace this with an actual Todo ID to test
    try_get_todo_by_id(todo_id_to_test)
    
    # You can also try with a random ID that doesn't exist
    random_id = "some-random-id"
    try_get_todo_by_id(random_id)

    # Test Remove Todo
    print("\nRemove Todo with ID:")
    removed_todo = remove_todo("8af52e54045b423aabaa9bcf7003ff4d")  # Try with a valid ID
    if removed_todo:
        print(f"Todo {removed_todo} removed.")
    else:
        print("Todo not found for removal.")

    # Test Update Todo
    print("\nUpdate Todo with ID:")
    updated_todo = update_todo("7f3d774efcad4dcbbccd891c2b121860", {"title": "Updated Todo Title"})
    if updated_todo:
        print(f"Todo {updated_todo} updated.")
    else:
        print("Todo not found for update.")
