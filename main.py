import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.user_models import UserIn, UserOut, UserAct
from parcus_db.db_usuarios import get_usuario, update_usuario

api = FastAPI()


@api.get("/user/data/{id_usuario}") ## El get se envía a través de la URL
async def get_data(id_usuario: int):

    user_in_db = get_usuario(id_usuario)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    user_out = UserOut(**user_in_db.dict())

    return  user_out



@api.put("/user/actualiza/")
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
    
    update_usuario(user_in_db)
    user_out = UserOut(**user_in_db.dict())

    return  user_out