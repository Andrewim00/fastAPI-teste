from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.responses import FileResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

template = Jinja2Templates(directory="viewers")

class SensorData(BaseModel):
    distance: float = 9


vaga_status = "Livre"


@app.post("/dados")
async def receber_dados(dados: SensorData):
    global vaga_status

    if dados.distance < 10:
        vaga_status = "Ocupada"
    else:
        vaga_status = "Livre"
    
    return {"status": vaga_status}


@app.get("/")
async def read_index(request: Request):
    return template.TemplateResponse("exibir.html", {"request": request, "vaga_status": vaga_status})


@app.get("/status")
async def status_vaga():
    return {"vaga": vaga_status}