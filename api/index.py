from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

template = Jinja2Templates(directory="templates")

class SensorData(BaseModel):
    id: int
    ocupado: bool = False


vaga_status = "Livre"


@app.post("/dados")
async def receber_dados(dados: SensorData):
    global vaga_status

    if dados.ocupado:
        vaga_status = "Ocupada"
    else:
        vaga_status = "Livre"
    
    return {"status": vaga_status}


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return template.TemplateResponse("index.html", {"request": request, "vaga_status": vaga_status})


@app.get("/status")
async def status_vaga():
    return {"vaga": vaga_status}