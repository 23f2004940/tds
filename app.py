import json
from urllib.parse import parse_qs

# Load student marks from local JSON
with open("marks.json") as f:
    data = json.load(f)
marks_map = {s["name"]: s["marks"] for s in data}

def handler(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"

    query = parse_qs(request.query_string.decode())
    names = query.get("name", [])

    marks = [marks_map.get(name, 0) for name in names]
    return response.json({"marks": marks})
