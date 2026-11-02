from sqlalchemy import Column, Integer, Text,Boolean
from app.db.session import Base



class country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True, index=True)
    Code = Column(Text,nullable=False)
    Name = Column(Text,nullable=False)
    status = Column(Boolean,nullable=False)

