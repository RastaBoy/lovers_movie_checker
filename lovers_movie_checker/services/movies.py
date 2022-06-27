from .abc import CRUDServiceInterface
from ..db.models.movie import Movie

class MovieService(CRUDServiceInterface):
    handled_model = Movie
    
    ...