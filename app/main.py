from fastapi import FastAPI

from app.routers import auth, user, task, project, priority, category

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(task.router, prefix="/tasks", tags=["tasks"])
app.include_router(project.router, prefix="/projects", tags=["projects"])
app.include_router(priority.router, prefix="/priorities", tags=["priorities"])
app.include_router(category.router, prefix="/categories", tags=["categories"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
