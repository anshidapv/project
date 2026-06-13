from fastapi import APIRouter
router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)
tasks = []
@router.get("/")
def get_tasks():
    return tasks
@router.post("/")
def create_task(task: dict):
    task["id"] = len(tasks) + 1
    tasks.append(task)
    return {
        "message": "Task created",
        "task": task
    }
@router.get("/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"message": "Task not found"}
@router.put("/{task_id}")
def update_task(
    task_id: int,
    updated_task: dict
):
    for task in tasks:
        if task["id"] == task_id:
            task.update(updated_task)
            return {
                "message": "Task updated",
                "task": task
            }
    return {"message": "Task not found"}
@router.delete("/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {
                "message": "Task deleted"
            }
    return {"message": "Task not found"}