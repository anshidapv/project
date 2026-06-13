from fastapi import APIRouter
router = APIRouter(
    prefix="/users",
    tags=["users"]
)
users = []
@router.get("/")
def get_users():
    return users
@router.get("/{user_id}")
def get_user(user_id: int):
    if user_id >= len(users):
        return {"message": "user not found"}
    return users[user_id]
@router.post("/")
def create_user(user: dict):
    user["id"] = len(users)
    users.append(user)
    return {
         "message": "user created",
         "user": user
    }
@router.delete("/{user_id}")
def delete_user(user_id: int):
    if user_id >= len(users):
        return {"message": "user not found"}
    deleted_user = users.pop(user_id)
    return {
        "message": "user deleted",
            "user": deleted_user
    }