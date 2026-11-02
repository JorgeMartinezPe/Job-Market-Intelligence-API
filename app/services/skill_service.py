from typing import List

from app.models.skill import Skill
<<<<<<< HEAD
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
=======


def get_or_create_skills(db, skill_names):
    skills = []
    seen = set()

    for skill_name in skill_names or []:
        name = skill_name.strip().lower()
        if not name or name in seen:
            continue
        seen.add(name)

        skill = db.query(Skill).filter(Skill.name == name).first()

        if not skill:
            skill = Skill(name=name)
            db.add(skill)
            db.flush()

        skills.append(skill)

    return skills
>>>>>>> eccfe6b12233fb220f13d162ecbea7c7868cc263
