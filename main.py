# main.py
from fastapi import FastAPI, Request
from pydanic import BaseModel
app = FastAPI()

tarefas = [{"id_tarefa": "1",
           "descricao": "semana 13 aula 2"}]

class Tarefa(BaseModel):
     id_tarefa: float
     titulo: str
     descricao: str

@app.get("/tarefa/{id_tarefa}")
async def ListarTarefaPorID(id_tarefa):
    for tarefa in tarefas:
      if tarefa["id_tarefa"] == id_tarefa:
         tarefa.remove(tarefa)
         return "tarefa excluida"
    
  
@app.get("/tarefas")
def ListarTarefas():
    return tarefas

@app.post("/tarefas")
def CadastrarTarefa(tarefa: Tarefa):
    tarefas.append({"titulo": tarefa.titulo, "descricao": tarefa.descricao})
    
# @app.delete("/tarefa")
# def DeletarTarefa(titulo):