from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .. import Base

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    
    creator_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    creator = relationship('User', uselist=False)
