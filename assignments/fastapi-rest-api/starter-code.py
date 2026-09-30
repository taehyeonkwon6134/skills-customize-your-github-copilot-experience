from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Todo API")


todos = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
]


class TodoCreate(BaseModel):
    title: str
    completed: bool = False


@app.get("/todos")
def get_todos():
    # TODO: Return all todo items.
    pass


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    # TODO: Find the requested todo and return it.
    # Raise HTTPException with status.HTTP_404_NOT_FOUND if it does not exist.
    pass


@app.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate):
    # TODO: Create a unique ID, add the new todo, and return it.
    pass


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    # TODO: Remove the requested todo and return a confirmation message.
    # Raise HTTPException with status.HTTP_404_NOT_FOUND if it does not exist.
    pass
