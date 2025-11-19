from fastapi import FastAPI
from app.api.v1 import projects

app = FastAPI(title="Smart Task Manager API")

# Include routers with prefixes and tags
# app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
# app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["tasks"])
app.include_router(projects.router, prefix="/api/v1/projects", tags=["projects"])

# Optional root route
@app.get("/")
def root():
    return {"message": "Welcome to Smart Task Manager API"}
