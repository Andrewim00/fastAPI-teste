from fastapi import FastAPI, Request, BackgroundTasks
from pydantic import BaseModel
from starlette.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

template = Jinja2Templates(directory="templates")

class SensorData(BaseModel):
    id: int
    ocupado: bool = True


vaga_status = "Livre"

def atualizar_vaga(novo_status: str):
    global vaga_status
    vaga_status = novo_status


@app.post("/dados")
async def receber_dados(dados: SensorData, task: BackgroundTasks):
    if dados.ocupado == True:
        nova_vaga = "Ocupada"
    else:
        nova_vaga = "Livre"

    task.add_task(atualizar_vaga, nova_vaga)
    return {"status": vaga_status}


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return template.TemplateResponse("index.html", {"request": request, "vaga_status": vaga_status})


@app.get("/status")
async def status_vaga():
    return {"vaga": vaga_status}