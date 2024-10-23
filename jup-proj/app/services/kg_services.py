import os
from unstructured.partition.pdf import partition_pdf
from unstructured.partition.docx import partition_docx
from unstructured.partition.pptx import partition_pptx
from graphrag_sdk.source import Source
from graphrag_sdk import KnowledgeGraph, Ontology
from graphrag_sdk.models.openai import OpenAiGenerativeModel
from graphrag_sdk.model_config import KnowledgeGraphModelConfig
from app.config import settings

# Define directories
pdf_directory = "Data/PDFS"
docx_directory = "Data/DOCX"
pptx_directory = "Data/PPTX"


# Function to process PDF, DOCX, and PPTX files
def process_files(directory, extension, partition_func):
    sources = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            file_path = os.path.join(directory, filename)
            elements = partition_func(filename=file_path)

            txt_filename = os.path.splitext(filename)[0] + ".txt"
            txt_path = os.path.join(directory, txt_filename)

            with open(txt_path, "w", encoding="utf-8") as txt_file:
                for element in elements:
                    if element.text:
                        txt_file.write(element.text + "\n")

            sources.append(Source(txt_path))
    return sources


# Function to initialize knowledge graph
def initialize_knowledge_graph():
    pdf_sources = process_files(pdf_directory, ".pdf", partition_pdf)
    docx_sources = process_files(docx_directory, ".docx", partition_docx)
    pptx_sources = process_files(pptx_directory, ".pptx", partition_pptx)

    all_sources = pdf_sources + docx_sources + pptx_sources

    model = OpenAiGenerativeModel(model_name="gpt-4o")
    ontology = Ontology.from_sources(sources=all_sources, model=model)

    kg = KnowledgeGraph(
        name="K_G_A",
        model_config=KnowledgeGraphModelConfig.with_model(model),
        ontology=ontology,
        host=settings.FALKOR_HOST,
        username=settings.FALKOR_USERNAME,
        password=settings.FALKOR_PASSWORD,
        port=settings.FALKOR_PORT,
    )

    kg.process_sources(all_sources)
    return kg


# Function to ask a question to the knowledge graph
def ask_question(kg, question: str):
    chat = kg.chat_session()
    return chat.send_message(question)
