from fastapi import FastAPI

from pydantic import BaseModel, Field

class RecadoEntrada(BaseModel):
    texto: str = Field(min_length=1)

app = FastAPI()

recados = []

@app.get("/recados")
def listar_recados():
    return recados

@app.get("/")
def inicio():
    return {"mensagem": "API de recados"}

@app.post("/recados", status_code=201)
def criar_recado(recado: RecadoEntrada):
    novo_recado = {
        "id": len(recados) + 1,
        "texto": recado.texto
    }
    recados.append(novo_recado)
    return novo_recado