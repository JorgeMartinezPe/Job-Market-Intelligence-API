from pydantic import BaseModel
from typing import Optional


class CompanyCreate(BaseModel):
    name: Optional[str] = None
    industry: Optional[str] = None
    size: Optional[str] = None
    website: Optional[str] = None


class CompanyResponse(BaseModel):
<<<<<<< HEAD
    id:int
    name:str
=======
    id: int
    name: Optional[str] = None
>>>>>>> eccfe6b12233fb220f13d162ecbea7c7868cc263
    industry: Optional[str] = None
    size: Optional[str] = None
    website: Optional[str] = None
    model_config = {
        "from_attributes": True
    }


class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    industry: Optional[str] = None
    size: Optional[str] = None
    website: Optional[str] = None
