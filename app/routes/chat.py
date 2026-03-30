from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.chat_model import ChatRequest, ChatResponse
from app.services.chat_services import chat, get_chat_history, delete_chat_history
from app.utils.dependencies import get_current_user
from app.models.user_db_model import User
from app.database import get_db

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/", response_model=ChatResponse)
def run_chat(
    request: ChatRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    reply = chat(user_id=current_user.id, message=request.message, db=db)
    return ChatResponse(response=reply)

@router.get("/chat/history")
def get_chat_history_route(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    limit: int = 50,
    offset: int = 0
):
    history = get_chat_history(db, current_user.id, limit, offset)
    return history

@router.delete("/chat/history")
def delete_chat_history_route(current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db))-> dict:
    delete_response = delete_chat_history(db,current_user.id)
    return delete_response


