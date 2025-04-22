from fastapi import FastAPI, Request, status
from pydantic import BaseModel
from starlette.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

template = Jinja2Templates(directory="templates")

class SensorData(BaseModel):
    id: int
    ocupado: bool = True


vaga_status: str = "Livre"


@app.put("/dados")
async def receber_dados(dados: SensorData):
    global vaga_status

    if dados.ocupado:
        nova_vaga = "Ocupada"
    else:
        nova_vaga = "Livre"

    vaga_status = nova_vaga
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return template.TemplateResponse("index.html", {"request": request, "vaga_status": vaga_status})


@app.get("/status")
async def status_vaga():
    return {"vaga": vaga_status}