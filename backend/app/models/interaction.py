from sqlalchemy import Column, Integer, String, Text, DateTime, Date, ForeignKey, Enum, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.session import Base
import enum

class InteractionType(str, enum.Enum):
    call = "call"
    meeting = "meeting"
    email = "email"
    lunch = "lunch"
    conference = "conference"
    other = "other"

class Sentiment(str, enum.Enum):
    positive = "positive"
    neutral = "neutral"
    negative = "negative"

class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True, index=True)
    hcp_id = Column(Integer, ForeignKey("hcp.id", ondelete="CASCADE"), nullable=False)
    interaction_type = Column(Enum(InteractionType), nullable=False)
    interaction_date = Column(Date, nullable=False)
    duration_minutes = Column(Integer)
    notes = Column(Text)
    ai_summary = Column(Text)
    extracted_entities = Column(JSON)
    sentiment = Column(Enum(Sentiment), default=Sentiment.neutral)
    follow_up_date = Column(Date)
    logged_by = Column(Integer)
    logged_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    hcp = relationship("HCP")
