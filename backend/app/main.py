from fastapi import FastAPI
from app.api.v1 import projects, tasks, users
from app.core.exception_handlers import register_exception_handlers

app = FastAPI(title="Smart Task Manager API")

register_exception_handlers(app)

# Include routers with prefixes and tags
app.include_router(users.router, prefix="/api/v1", tags=["users"])
app.include_router(tasks.router, prefix="/api/v1", tags=["tasks"])
app.include_router(projects.router, prefix="/api/v1", tags=["projects"])

# Optional root route
@app.get("/")
def root():
    return {"message": "Welcome to Smart Task Manager API"}
