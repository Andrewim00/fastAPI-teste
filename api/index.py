from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse 

app = FastAPI()


class SensorData(BaseModel):
    distance: float


vaga_status = "Livre"


@app.post("/")
async def receber_dados(dados: SensorData):
    global vaga_status

    if dados.distance < 10:
        vaga_status = "Ocupada"
    else:
        vaga_status = "Livre"
    
    return {"status": vaga_status}


@app.get("/")
async def read_index():
    return FileResponse('viewers/index.html')


@app.get("/status")
async def status_vaga():
    return {"vaga": vaga_status}