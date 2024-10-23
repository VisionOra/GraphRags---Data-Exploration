import os
import random
from unstructured.partition.pdf import partition_pdf
from unstructured.partition.docx import partition_docx
from unstructured.partition.pptx import partition_pptx
from graphrag_sdk.source import Source
from falkordb import FalkorDB
from graphrag_sdk import KnowledgeGraph, Ontology
from graphrag_sdk.models.openai import OpenAiGenerativeModel
from graphrag_sdk.model_config import KnowledgeGraphModelConfig  # Corrected this part


def create_ontology(sources):
    model = OpenAiGenerativeModel(model_name="gpt-4o")
    ontology = Ontology.from_sources(
        sources=sources,
        model=model,
    )
    return ontology, model


def create_knowledge_graph(ontology, model, host, username, password, port):
    kg = KnowledgeGraph(
        name="K_G_A",
        model_config=KnowledgeGraphModelConfig.with_model(model),
        ontology=ontology,
        host=host,
        username=username,
        password=password,
        port=port,
    )
    return kg


def process_sources(kg, sources):
    kg.process_sources(sources)
    print("Knowledge Graph created:")
    print(kg._name)
    print(kg.db.list_graphs())
    return kg
