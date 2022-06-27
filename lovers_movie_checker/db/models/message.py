from enum import Enum

from sqlalchemy import Column, String, Integer, ForeignKey, Enum as DBEnum
from sqlalchemy.orm import relationship

from .. import Base

class MessageType(Enum):
    PAIR_CREATION = 'PAIR_CREATION'
    APPROVE = 'APPROVE'


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, autoincrement=True)

    sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    sender = relationship('User', uselist=False)

    text = Column(String, nullable=False)
    type = Column(DBEnum(MessageType), nullable=False)

    destination_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    destination = relationship('User', uselist=False)