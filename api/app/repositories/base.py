from typing import Generic, TypeVar, Type, Optional, List
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType],db: Session):
        self.model = model
        self.db = db

    def get_by_id(self, id: int) -> Optional[ModelType]:
        return self.db.query(self.model).filter(self.model.id == id).first()
    
    def get_all(self) -> List[ModelType]:
        return self.db.query(self.model).all()
    
    def save(self, instance: ModelType) -> ModelType:
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance