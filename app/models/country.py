from sqlalchemy import Column, Integer, String, Text
from app.db.session import Base



class country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True, index=True)
    code_mx = Column (Text, index=True, nullable=False)
    currency_code = Column(Text,nullable=False)
    denomination = Column(String,nullable=False)

