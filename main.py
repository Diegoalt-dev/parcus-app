import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.user_models import UserIn, UserOut, UserAct
from parcus_db.db_usuarios import get_usuario, update_usuario
from parcus_db.db_transaction import get_transaction, add_transaction
from models.transaction_models import TransactionIn, TransactionOut
import json
from fastapi.middleware.cors import CORSMiddleware

origins = [
"http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
"http://localhost", "http://localhost:8080", "https://parcus-app.herokuapp.com", 
"http://parcus-app.herokuapp.com",
]



api = FastAPI()

api.add_middleware(
CORSMiddleware, allow_origins=origins,
allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)


@api.post("/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_usuario(user_in.id_usuario)
    if user_in_db == None:
        raise HTTPException(status_code=404,
        detail="El usuario no existe")
    if user_in_db.password != user_in_db.password:
        raise HTTPException(status_code=403,
        detail="Error de autenticacion")
    return {"Autenticado": True}


@api.get("/user/data/{id_usuario}") ## El get se envía a través de la URL
async def get_data(id_usuario: int):

    user_in_db = get_usuario(id_usuario)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    user_out = UserOut(**user_in_db.dict())

    return user_out



@api.post("/user/actualiza/")
async def actualiza_data(user_act: UserAct):

    user_in_db = get_usuario(user_act.id_usuario)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_act.nombre != None:
        user_in_db.nombre = user_act.nombre
    if user_act.ctaBancaria != None:
        user_in_db.ctaBancaria = user_act.ctaBancaria
    if user_act.tarjCredito != None:
        user_in_db.tarjCredito = user_act.tarjCredito
    if user_act.efectivo != None:
        user_in_db.efectivo = user_act.efectivo
    
    update_usuario(user_in_db)
    user_out = UserOut(**user_in_db.dict())

    return  user_out

@api.post("/user/add/ingreso/")
async def agregar_ingreso_fijo(transaction_in:TransactionIn):
    if transaction_in.valor == 0:
        raise HTTPException(status_code=402, detail="Valor incorrecto")
    transacciones = get_transaction(transaction_in.id_usuario)
    if transacciones == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    add_transaction(transaction_in)
    
    return "Transacción agregada"

@api.get("/transaction/data/{id_usuario}") ## El get se envía a través de la URL
async def obtener_transaction(id_usuario: int):
    transacciones= get_transaction(id_usuario)
    
    if transacciones == None:
        raise HTTPException(status_code=404, detail="El usuario no existe") 
    
    transaction_out = TransactionOut(**{"id_usuario":id_usuario,"transacciones":transacciones})

    return transaction_out

    
    