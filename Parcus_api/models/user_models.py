from pydantic import BaseModel

class UserIn(BaseModel):
    id_usuario: int
    nombre: str

class UserOut(BaseModel):
    nombre: str
    ctaBancaria: str
    tarjCredito: str
    efectivo: int  