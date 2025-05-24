from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks.json once at startup
with open("marks.json") as f:
    students = json.load(f)
marks_map = {s["name"]: s["marks"] for s in students}

@app.get("/api")
async def get_marks(request: Request):
    query_params = request.query_params.getlist("name")
    marks = [marks_map.get(name, 0) for name in query_params]
    return JSONResponse(content={"marks": marks})
