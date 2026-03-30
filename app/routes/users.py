from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.user_services import register_user, login_user

router = APIRouter(prefix="/users", tags=["Users"])

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/register")
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    user = register_user(request.username, request.email, request.password, db)
    if user is None:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    return {"message": "User registered successfully", "user_id": user.id}

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    token = login_user(request.email, request.password, db)
    if token is None:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"access_token": token, "token_type": "bearer"}