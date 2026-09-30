# 📘 Assignment: FastAPI REST API

## 🎯 Objective

Build a small REST API with FastAPI to practice routing, JSON request and response data, validation with Pydantic, and HTTP status codes.

## 📝 Tasks

### 🛠️ Create the API and Read Endpoints

#### Description

Use the provided starter code to create a FastAPI application for managing an in-memory list of todo items.

#### Requirements

Completed program should:

- Create a FastAPI application instance named `app`.
- Return all todo items from `GET /todos` as JSON.
- Return one todo item from `GET /todos/{todo_id}`.
- Return a `404` response when the requested todo does not exist.
- Include automatic API documentation available at `/docs`.


### 🛠️ Add and Validate Todo Items

#### Description

Define a Pydantic model for new todo items and implement an endpoint that validates incoming JSON data before adding it to the in-memory list.

#### Requirements

Completed program should:

- Define a request model with a required title and a boolean `completed` field.
- Add a new todo through `POST /todos`.
- Assign a unique integer ID to each new todo.
- Return the created todo as JSON with a `201 Created` status code.
- Reject requests that do not provide a valid title or valid field types.

Example request:

```json
{
  "title": "Practice FastAPI",
  "completed": false
}
```


### 🛠️ Update and Delete Todo Items

#### Description

Complete the remaining item-management endpoint so clients can remove a todo and receive an appropriate response when the item is missing.

#### Requirements

Completed program should:

- Delete a todo through `DELETE /todos/{todo_id}`.
- Return a confirmation message after a successful deletion.
- Return a `404` response when attempting to delete a todo that does not exist.
- Keep the API responses in JSON format.

Run the API with:

```bash
pip install fastapi uvicorn
uvicorn starter-code:app --reload
```

Then open `http://127.0.0.1:8000/docs` to test the endpoints interactively.
