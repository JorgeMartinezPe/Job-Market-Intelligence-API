from app.models.skill import Skill
from sqlalchemy.orm import Session

def get_or_create_skills(db, skill_names):
    skills = []

    for skill_name in skill_names:
        skill = db.query(Skill).filter(Skill.name == skill_name).first()

        if not skill:
            skill = Skill(name=skill_name)
            db.add(skill)
            db.flush()

        skills.append(skill)

    return skills