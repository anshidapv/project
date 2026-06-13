from fastapi import FastAPI
from router.users import router as users_router
from router.tasks import router as tasks_router
from auth import router as auth_router
app = FastAPI(
    title="Personal Task Manager API",
    description="Task Manager Backend usinf FastAPI and SQLite",
    version="1.0.0"
)
app.include_router(users_router)
app.include_router(tasks_router)
app.include_router(auth_router)
@app.get("/")
def home():
    return{
        "message": "Personal Task Manager API Running Successfully"
    }
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }