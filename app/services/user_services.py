from sqlalchemy.orm import Session
from app.models.user_db_model import User
from app.utils.security import hash_password, verify_password
from app.utils.auth import create_token

def register_user(username: str, email: str, password: str, db: Session):
    existing = db.query(User).filter(
        (User.username == username) | (User.email == email)
    ).first()

    if existing:
        return None

    new_user = User(
        username=username,
        email=email,
        hashed_password=hash_password(password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login_user(email: str, password: str, db: Session):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    token = create_token(user.id)
    return token