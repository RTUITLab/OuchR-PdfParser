import io
import os
import requests

from lxml import etree
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from bs4 import BeautifulSoup

from typing import Optional
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


def extract_text_from_pdf(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    ff = os.path.basename(file.filename)
    with open(ff, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    converter.close()
    fake_file_handle.close()

    if text:
        return text

@app.get("/")
async def root():
    r = requests.get("https://edu.greenatom.ru/")  # url - ссылка
    htmls = r.text
    htmlparser = etree.HTMLParser()
    tree = etree.parse(htmls, htmlparser)
    images = tree.find_all('form')
    return images

@app.post("/getInter")
async def getInter(file: UploadFile = File(...)):
    str = extract_text_from_pdf(file)
    return str