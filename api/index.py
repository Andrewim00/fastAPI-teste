from fastapi import FastAPI, Request, status
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

    for i in range(len(vaga_status)):
        if dados.vagas[i+1]:
            vaga_status[i + 1] = "Ocupado"
        else:
            vaga_status[i + 1] = "Livre"


    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return template.TemplateResponse("index.html", {"request": request, "vaga_status": vaga_status})


@app.get("/status")
async def status_vaga():
    return {"vaga": vaga_status}