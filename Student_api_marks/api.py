from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

# Load JSON file
JSON_FILE = "q-vercel-python.json"
with open(JSON_FILE, "r") as file:
    data = json.load(file)

app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api")
async def get_marks(name: list[str] = Query([])):
    marks = [entry["marks"] for entry in data if entry["name"] in name]
    return {"marks": marks}
