from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Load templates from the 'templates' folder
templates = Jinja2Templates(directory="templates")

@app.get("/status")
def get_status():
    return {"message": "KonectIQ is online"}

@app.get("/dashboard", response_class=HTMLResponse)
def read_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
