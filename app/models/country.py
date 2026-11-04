from sqlalchemy import Column, Integer, Text,Boolean
from app.db.session import Base



class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(Text,nullable=False,unique=True)
    name = Column(Text,nullable=False,unique=True)
    status = Column(Boolean,nullable=False)

