from sqlalchemy.orm import Session
from typing import Optional

from app.models.study_plan import StudyPlan
from app.repositories.base import BaseRepository


class StudyPlanRepository(BaseRepository[StudyPlan]):
    def __init__(self, db: Session):
        super().__init__(StudyPlan, db)