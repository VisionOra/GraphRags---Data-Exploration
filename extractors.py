import os
from unstructured.partition.pdf import partition_pdf
from unstructured.partition.docx import partition_docx
from unstructured.partition.pptx import partition_pptx
from graphrag_sdk.source import Source


def extract_text(directory, partition_function, file_extension):
    sources = []
    for filename in os.listdir(directory):
        if filename.endswith(file_extension):
            file_path = os.path.join(directory, filename)
            elements = partition_function(filename=file_path)

            # Save extracted text to .txt file
            txt_filename = os.path.splitext(filename)[0] + ".txt"
            txt_path = os.path.join(directory, txt_filename)

            with open(txt_path, "w", encoding="utf-8") as txt_file:
                for element in elements:
                    if element.text:
                        txt_file.write(element.text + "\n")

            sources.append(Source(txt_path))
    return sources


def extract_pdf_text(pdf_directory):
    return extract_text(pdf_directory, partition_pdf, ".pdf")


def extract_docx_text(docx_directory):
    return extract_text(docx_directory, partition_docx, ".docx")


def extract_pptx_text(pptx_directory):
    return extract_text(pptx_directory, partition_pptx, ".pptx")
