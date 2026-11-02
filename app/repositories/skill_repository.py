from typing import Optional

from sqlalchemy.orm import Session

from app.models.skill import Skill
from app.repositories.base_repository import BaseRepository


class SkillRepository(BaseRepository[Skill]):
    def __init__(self, db: Session):
        super().__init__(db, Skill)

    def find_by_name(self, name: str) -> Optional[Skill]:
        return self.db.query(Skill).filter(Skill.name == name).first()
