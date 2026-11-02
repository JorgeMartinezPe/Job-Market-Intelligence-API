from typing import List

from app.models.skill import Skill
from app.repositories.skill_repository import SkillRepository


class SkillService:
    def __init__(self, repository: SkillRepository):
        self.repository = repository

    def get_or_create_many(self, skill_names: List[str]) -> List[Skill]:
        skills = []
        for skill_name in skill_names:
            skill = self.repository.find_by_name(skill_name)
            if not skill:
                skill = self.repository.add(Skill(name=skill_name))
            skills.append(skill)
        return skills
