from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "resources.json"


app = FastAPI()
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "app" / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "app" / "templates"))




def load_resources():
try:
with open(DATA_PATH, "r", encoding="utf-8") as f:
return json.load(f)
except Exception:
return []




@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
resources = load_resources()
# Optionally sort by year or title
resources = sorted(resources, key=lambda r: (-r.get("year", 0), r.get("title", "")))
return templates.TemplateResponse("index.html", {"request": request, "resources": resources})




@app.get("/api/resources")
async def api_resources():
return load_resources()
