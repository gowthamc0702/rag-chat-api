from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.database import engine
from app.models import user_db_model, chat_db_model ,chat_embedding_model
from app.routes import users, chat

user_db_model.Base.metadata.create_all(bind=engine)
chat_db_model.Base.metadata.create_all(bind=engine)
chat_embedding_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(chat.router)

@app.get("/")
def home():
    return {"message": "AI Backend Platform Running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}