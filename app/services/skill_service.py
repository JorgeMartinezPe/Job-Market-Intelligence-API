from typing import List

from app.models.skill import Skill
from app.repositories.skill_repository import SkillRepository


class SkillService:
    def __init__(self, repository: SkillRepository):
        self.repository = repository

