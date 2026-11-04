from pydantic import BaseModel, Field,ConfigDict
from typing import Optional, List


class CountryCreate(BaseModel):
    code: str # El que no tenga el = None lo convierte en obligatorio
    name: str
    status: bool


class CountryResponse(BaseModel):
    id : int
    code: Optional[str]
    name: Optional[str]
    status: Optional[bool]
    model_config = ConfigDict(from_attributes=True)

class CountryUpdate(BaseModel):
    code: Optional[str] = None
    name: Optional[str]  = None # El que tenga None hace que se necesite verificar que al actualizarlo, para no mandar datos vacios 
    status: Optional[bool]  = None

