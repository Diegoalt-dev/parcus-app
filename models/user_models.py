from pydantic import BaseModel

class UserIn(BaseModel):
    id_usuario: int
    nombre: str

class UserOut(BaseModel):
    nombre: str
    ctaBancaria: tuple[str,int]
    tarjCredito: tuple[str,int]
    efectivo: int