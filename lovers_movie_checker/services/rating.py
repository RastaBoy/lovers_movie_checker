from .abc import CRUDServiceInterface
from ..db.models.rating import Rating

class RatingService(CRUDServiceInterface):
    handled_model = Rating
    
    ...