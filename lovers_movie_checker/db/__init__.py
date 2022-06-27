from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base

import os

engine = create_engine(f'sqlite:///{os.path.join(os.getcwd(), "database.db")}')
Base = declarative_base(bind=engine)

from .models import *

Base.metadata.create_all()


def session_factory():
    return orm.scoped_session(
        orm.sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine
        )
    )