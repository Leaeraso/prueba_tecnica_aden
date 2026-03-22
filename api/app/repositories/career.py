from sqlalchemy.orm import Session
from typing import Optional

from app.models.career import Career
from app.repositories.base import BaseRepository


class CareerRepository(BaseRepository[Career, int]):
    def __init__(self, db: Session):
        super().__init__(Career, db)
        