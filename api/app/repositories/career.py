from sqlalchemy.orm import Session

from app.models.career import Career
from app.repositories.base import BaseRepository


class CareerRepository(BaseRepository[Career]):
    def __init__(self, db: Session):
        super().__init__(Career, db)
        