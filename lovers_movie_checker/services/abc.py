from abc import ABC
from sqlalchemy.exc import ProgrammingError

from ..db import session_factory, Base

class CRUDServiceInterface(ABC):
    handled_model = None

    def __init__(self) -> None:
        self.session = session_factory()

    def __del__(self):
        try:
            self.session.close()
        except ProgrammingError:
            pass

    def get_all(self):
        return self.session.query(self.handled_model).all()

    def get(self, subject_ident:str=None, name:str=None):
        return self.session.query(self.handled_model).filter(self.handled_model.id == subject_ident).first() if name is None else self.session.query(self.handled_model).filter(self.handled_model.name == name).first()

    def create(self, instance: Base):
        if not isinstance(instance, Base):
            raise TypeError(f'Instance of {type(instance)} cannot be handled by {self.handled_model} service.')
        self.session.add(instance)
        self.session.flush()
        self.session.commit()
        return object

    def update(self, instance: Base):
        if not isinstance(instance, Base):
            raise TypeError(f'Instance of {type(instance)} cannot be handled by {self.handled_model} service.')
        self.session.merge(instance)
        # self.session.flush()
        self.session.commit()
        return self.get(subject_ident=instance.id)

    def delete(self, subject_ident):
        object = self.get(subject_ident=subject_ident)
        self.session.delete(object)
        self.session.commit()