from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

template = Jinja2Templates(directory="templates")

class SensorData(BaseModel):
    vagas: dict[str, bool]


vaga_status: dict[int, str] = {
    1: "Livre",
    2: "Livre",
    3: "Livre",
    4: "Livre"
}


@app.put("/dados")
async def receber_dados(dados: SensorData):
    global vaga_status

    for key in vaga_status:
        if dados.vagas[str(key)]:
            vaga_status[key] = "Ocupado"
        else:
            vaga_status[key] = "Livre"


    return {"message": "Updated successfully"}


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return template.TemplateResponse("index.html", {"request": request, "vaga_status": vaga_status})


@app.get("/status")
async def status_vaga():
    return {"vaga": vaga_status}