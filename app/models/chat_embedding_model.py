from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime
from datetime import datetime, timezone
from app.database import Base
from pgvector.sqlalchemy import Vector

class ChatEmbedding(Base):
    __tablename__ = "chat_embeddings"

    id = Column(Integer, primary_key=True, index=True)

    message_id = Column(Integer, ForeignKey("chat_messages.id",ondelete="CASCADE"), nullable=False)

    embedding = Column(Vector(1024), nullable=False)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))