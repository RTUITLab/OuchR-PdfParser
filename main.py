import io
import os
import sys
import threading

import requests

from lxml import etree
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from bs4 import BeautifulSoup

from typing import Optional
from fastapi import FastAPI, File, UploadFile
sys.setrecursionlimit(100000)
threading.stack_size(0x2000000)
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

def getCountries():
    r = requests.get("https://edu.greenatom.ru/")  # url - ссылка
    htmls = r.text
    strr = htmls.split('form')[2]
    all = strr.split('\" >')
    list_el = []
    for i in all:
        list_el += [i.split('</option>')[0]]
    list_el[0] = list_el[0].split("cted>")[1]
    return list_el



@app.get("/")
async def root():
    return getCountries()

@app.post("/getInter")
async def getInter(file: UploadFile = File(...)):
    str = extract_text_from_pdf(file)
    return str