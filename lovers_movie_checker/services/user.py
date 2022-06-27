from .abc import CRUDServiceInterface
from ..db.models.user import User

class UserService(CRUDServiceInterface):
    handled_model = User

    ...