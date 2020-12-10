from typing import Dict
from pydantic import BaseModel

class UsuariosDB(BaseModel):
    id_usuario: int
    nombre: str
    ctaBancaria: tuple[str, int]
    tarjCredito: tuple[str, int]
    efectivo: int

database_users = Dict[str, UsuariosDB]

database_users = {
    "Petronilo": UsuariosDB(**{ "id_usuario":12345678,
                                "nombre":"Petronilo",
                                "ctaBancaria":["Davivienda123",2000000],
                                "tarjCredito":["Visa123",1500000],
                                "efectivo":120000}),
    
    "Clementina": UsuariosDB(**{ "id_usuario":23456789,
                                "nombre":"Clementina",
                                "ctaBancaria":["Bancolombia123",3000000],
                                "tarjCredito":["MasterCard123",2000000],
                                "efectivo":3000000}),

    "Anacleta": UsuariosDB(**{ "id_usuario":34567890,
                                "nombre":"Anacleta",
                                "ctaBancaria":["CajaSocial123",2500000],
                                "tarjCredito":["Diners123",1000000],
                                "efectivo":5000000}),

    "Apolonio": UsuariosDB(**{ "id_usuario":45678901,
                                "nombre":"Apolonio",
                                "ctaBancaria":["Popular123",500000],
                                "tarjCredito":["American123",0],
                                "efectivo":2300000})
}

def get_user(id_usuario: int):
    if id_usuario in database_users.keys():
        return database_users[id_usuario]
    else:
        return None

def update_user(usuario_db: UsuariosDB):
    database_users[usuario_db.id_usuario] = usuario_db    
    return usuario_db

