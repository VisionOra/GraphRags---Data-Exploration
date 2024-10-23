from fastapi import APIRouter
from app.services.kg_services import initialize_knowledge_graph, ask_question

router = APIRouter()

# Sample URLs for the knowledge graph
urls = [
    "https://www.rottentomatoes.com/m/side_by_side_2012",
    "https://www.rottentomatoes.com/m/matrix",
    "https://www.rottentomatoes.com/m/matrix_revolutions",
    "https://www.rottentomatoes.com/m/matrix_reloaded",
    "https://www.rottentomatoes.com/m/speed_1994",
    "https://www.rottentomatoes.com/m/john_wick_chapter_4"
]

# Route for processing knowledge graph
@router.get("/ask/")
def ask_kg(question: str):
    kg = initialize_knowledge_graph(urls)
    answer = ask_question(kg, question)
    return {"answer": answer}
