from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    category = Column(String, nullable=False)
    content = Column(String, nullable=False)
    status = Column(String, default="Aberto")

    client = relationship("Client", back_populates="tickets")