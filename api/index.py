from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class SensorData(BaseModel):
    distance: float


vaga_status = "Livre"


@app.post("/dados")
async def receber_dados(dados: SensorData):
    global vaga_status

    if dados.distance < 10:
        vaga_status = "Ocupada"
    else:
        vaga_status = "Livre"
    
    return {"status": vaga_status}


@app.get("/status")
async def status_vaga():
    return {"vaga": vaga_status}