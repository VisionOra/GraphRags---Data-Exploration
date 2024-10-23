import os
from extractors import extract_pdf_text, extract_docx_text, extract_pptx_text
from knowledge_graph import create_ontology, create_knowledge_graph, process_sources
from chat import chat_with_knowledge_graph
import config

# Specify directories containing the files
pdf_directory = "Data/PDFS"
docx_directory = "Data/DOCX"
pptx_directory = "Data/PPTX"

# Extract text from files
pdf_sources = extract_pdf_text(pdf_directory)
docx_sources = extract_docx_text(docx_directory)
pptx_sources = extract_pptx_text(pptx_directory)

all_sources = pdf_sources + docx_sources + pptx_sources

# Create ontology
ontology, model = create_ontology(all_sources)

# Create and process knowledge graph
kg = create_knowledge_graph(
    ontology=ontology,
    model=model,
    host=config.FALKORDB_HOST,
    username=config.FALKORDB_USERNAME,
    password=config.FALKORDB_PASSWORD,
    port=config.FALKORDB_PORT,
)

# Process the sources
process_sources(kg, all_sources)

# Chat with the knowledge graph
response = chat_with_knowledge_graph(kg, "Enter your question Based on Data.")
print(response)
