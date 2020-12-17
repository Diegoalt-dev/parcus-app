from pydantic import BaseModel
from typing import Tuple, List


class TransactionIn(BaseModel):
    id_usuario: int
    concepto: str
    descripcion: str = None
    valor: float
    recurrencia: int = None

class TOutdata(BaseModel):
    id_usuario: int = None
    concepto: str = None
    descripcion: str = None
    valor: float = None
    recurrencia: int = None
    
class TransactionOut(BaseModel):
    id_usuario: int 
    transacciones: List[TOutdata]