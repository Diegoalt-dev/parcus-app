from pydantic import BaseModel
from typing import Tuple

class UserIn(BaseModel):
    id_usuario: int
    nombre: str

class UserOut(BaseModel):
    nombre: str
    ctaBancaria: Tuple[str,int]
    tarjCredito: Tuple[str,int]
    efectivo: int

class UserAct(BaseModel):
    id_usuario: int 
    nombre: str = None
    ctaBancaria: Tuple[str,int] = None
    tarjCredito: Tuple[str,int] = None
    efectivo: int = None
