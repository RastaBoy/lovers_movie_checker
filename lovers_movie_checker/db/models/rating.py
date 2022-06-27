from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .. import Base

class Rating(Base):
    __tablename__ = 'rating'

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', uselist=False)

    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)
    movie = relationship('Movie', uselist=False)
