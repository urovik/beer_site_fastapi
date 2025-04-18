from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    name: str
    description: str 
    manafacture: str
    type: str

class TypeSchema(BaseModel):
    type: str 

