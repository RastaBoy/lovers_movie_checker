from .abc import CRUDServiceInterface
from ..db.models.message import Message, MessageType


class MessageService(CRUDServiceInterface):
    handled_model = Message

    ...