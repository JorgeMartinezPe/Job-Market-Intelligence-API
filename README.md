# Job-Market-Intelligence-API
Una API REST production-ready que ingiere datasets de ofertas de trabajo tech, genera estadísticas por skill/rol/salario, y expone endpoints de predicción sobre qué tecnologías están en crecimiento. Con autenticación JWT, Docker, CI/CD, y documentación automática con Swagger.
# Job Market Intelligence API

API REST diseñada para analizar el mercado laboral tecnológico a partir de datasets de ofertas de empleo. Permite extraer insights sobre demanda de habilidades, salarios y tendencias, además de ofrecer predicciones sobre tecnologías en crecimiento.

---

## Motivación

El mercado tech cambia constantemente. Este proyecto busca responder preguntas como:

- ¿Qué tecnologías están en crecimiento?
- ¿Qué habilidades son más demandadas?
- ¿Cómo varían los salarios por rol?

---

##Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Docker
- GitHub Actions (CI/CD)

---

##Arquitectura

El proyecto sigue principios de separación de responsabilidades:
Client → API → Services → Repositories → Database
