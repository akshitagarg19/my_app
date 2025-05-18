import json
import os
from urllib.parse import parse_qs

def handler(request, response):
    # Enable CORS for all origins
    response.headers['Access-Control-Allow-Origin'] = '*'

    # Load the JSON file (one level above /api/)
    with open(os.path.join(os.path.dirname(__file__), '../data.json')) as f:
        raw_data = json.load(f)

    # Convert list to dictionary for faster lookup
    data_dict = {entry['name']: entry['marks'] for entry in raw_data}

    # Parse query parameters
    query = parse_qs(request.query_string.decode())
    names = query.get('name', [])  # support multiple ?name=X&name=Y

    # Get marks for each name in the order requested
    marks = [data_dict.get(name, None) for name in names]

    return response.json({"marks": marks})
