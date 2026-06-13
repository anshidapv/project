from fastapi import APIRouter
from database import conn, cursor
router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)
@router.post("/register")
def register(user: dict):
    cursor.execute(
        "INSERT INTO users (username,email,password)" \
        "VALUES(?,?,?)",
        (
            user["username"],
            user["email"],
            user["password"]
        )
    )
    conn.commit()
    return {"message": "User Registered Successfully"}
@router.post("/login")
def login(data: dict):
    cursor.execute(
        "SELECT*FROM users WHERE username=? AND password=?", 
        (
            data["username"],
            data["password"]
        )
    )
    user = cursor.fetchone()
    if user:
        return {"message": "Login Successful"}
    return {"message": "Invalid Username or Password"}