from fastapi import FastAPI
from app.api.v1 import users, tasks, projects

app = FastAPI(title="Smart Task Manager API")

app.include_router(users.router)
# app.include_router(tasks.router)
# app.include_router(projects.router)
