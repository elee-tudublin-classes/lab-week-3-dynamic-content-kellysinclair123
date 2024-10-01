# import dependencies
from fastapi import FastAPI, Request
from datetime import datetime
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import httpx
from contextlib import asynccontextmanager
import json
from starlette.config import Config

# Load environment variables from .env
config = Config(".env")



# create app instance
app = FastAPI()
  
# set location for templates
templates = Jinja2Templates(directory="app/view_templates")

# handle http get requests for the site root /
# return the index.html page
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    
    #get current date and time 
    serverTime: datetime = datetime.now().strftime("%d/%m/%y  %H:%M:%S")

    return templates.TemplateResponse("index.html", {"request": request, "serverTime": serverTime})
    

@app.get("/advice", response_class=HTMLResponse)
async def advice(request: Request):
    return templates.TemplateResponse("advice.html", {"request": request})

@app.get("/apod", response_class=HTMLResponse)
async def apod(request: Request):
    return templates.TemplateResponse("apod.html", {"request": request})

@app.get("/params", response_class=HTMLResponse)
async def params(request: Request, name : str | None =""):
    return templates.TemplateResponse("params.html", {"request": request, "name": name })

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

