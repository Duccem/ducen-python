from fastapi import FastAPI
from src.apps.api.controllers.tasks_controller import task_router

app = FastAPI()
app.include_router(prefix="/api", router=task_router)


@app.get("/")
def index():
    return {"message": "Welcome to my first api"}
