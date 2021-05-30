import io
import json
import os
import sys
import threading
from datetime import datetime

import convertapi as convertapi

import docker

import zoom
import outlook

import Text_NPL as tnpl
import requests
import uvicorn

from lxml import etree
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pydantic import BaseModel
from bs4 import BeautifulSoup

from typing import Optional, List
from fastapi import FastAPI, File, UploadFile
app = FastAPI()

import cloudconvert



from pdfreader import PDFDocument, SimplePDFViewer

def extract_text_from_pdf(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    ff = "C:/Users/sasha/PycharmProjects/docs_back/"+file.filename

    # convertapi.api_secret = 'cq1WdKvA1yGhTvYl'
    # convertapi.convert('txt', {
    #     'File': ff
    # }, from_format='pdf').save_files('C:/Users/sasha/PycharmProjects/docs_back/')

    with open('C:/Users/sasha/PycharmProjects/docs_back/Laptev_Ivan_Alexandrovich.txt', 'r', encoding='utf-8') as fh:
        text = fh.read()

    # with open(ff, 'rb') as fh:
    #     for page in PDFPage.get_pages(fh,
    #                                   caching=True,
    #                                   check_extractable=True):
    #         page_interpreter.process_page(page)
    #
    #     text = fake_file_handle.getvalue()
    #
    # converter.close()
    # fake_file_handle.close()

    os.remove("C:/Users/sasha/PycharmProjects/docs_back/"+file.filename)

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

class Item(BaseModel):
    name: str
    time: datetime
    duration: float
    password: Optional[str] = 'not-secure'

class InterItem(BaseModel):
    title: str
    skills: List[str] = []
    Competencies: str
    url: str
    id: str
    description: str

class Meet(BaseModel):
    zoom: str
    calendar: str

class Cont_answer(BaseModel):
    res: bool

class Cont_ask(BaseModel):
    image: str


@app.get("/")
async def root():
    return getCountries()

@app.get("/itemById", response_model=InterItem)
async def read_item(id: str = ""):
    with open('city.json', 'r', encoding='utf-8') as fp:
        city_data = fp.read()
        data = json.loads(city_data)
    for i in data:
        for j in i['topics']:
            if id in j['id']:
                return j

@app.post("/getInter", response_model=List[InterItem])
async def getInter(file: UploadFile = File(...)):
    str = ""
    if file.filename:
        # strip the leading path from the file name
        fn = "C:/Users/sasha/PycharmProjects/docs_back/"+file.filename
        open(fn, 'wb').write(file.file.read())
    str = extract_text_from_pdf(file)
    str = tnpl.getIntUrl(str)
    return str


@app.post("/addMeet", response_model=Meet)
async def getInter(item: Item):
    url = zoom.create_meet(item.name, item.time, item.duration, item.password)
    cal_url = outlook.addEvent(item.name, url, item.time, item.duration)
    return {"zoom": url, "calendar": cal_url}

@app.post("/runCont", response_model=Cont_answer)
async def runCont(cont: Cont_ask):
        return {docker.runCont("shureck/userback")}