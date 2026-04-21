from pydantic import BaseModel
from typing import Optional


class CompanyCreate(BaseModel):
    name:str
    industry: Optional[str] = None
    size: Optional[str] = None
    website: Optional[str] = None

class CompanyResponse(BaseModel):
    id:int
    name:str
    industry:str
    size:str
    website:str
    model_config = {
        "from_attributes": True
    }
class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    industry: Optional[str] = None
    size: Optional[str] = None
    website: Optional[str] = None