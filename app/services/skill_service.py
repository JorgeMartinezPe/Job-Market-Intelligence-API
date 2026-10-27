from app.models.skill import Skill


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
