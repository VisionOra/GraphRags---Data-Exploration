from fastapi import FastAPI
from app.routers import knowledge_graph

app = FastAPI()

app.include_router(knowledge_graph.router)

@app.get("/")
def root():
    return {"message": "FastAPI Knowledge Graph Project"}
