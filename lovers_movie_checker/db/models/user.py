from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4

from .. import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hash = Column(String, nullable=False, unique=True)
    nickname = Column(String(36))
    
    user_pair = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', uselist=False)

    photo_link = Column(String, nullable=True)