from fastapi import FastAPI
from src.apps.api.controllers.tasks_controller import task_router

app = FastAPI(root_path="/api")
app.include_router(router=task_router)


@app.get("/")
def index():
  return {"message": "Welcome to my first api"}
