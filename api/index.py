import json
import os
from urllib.parse import parse_qs

def handler(request, response):
    # --- Enable CORS ---
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    response.headers['Access-Control-Allow-Headers'] = '*'

    # Handle preflight requests (OPTIONAL: only needed if POST or other complex requests used)
    if request.method == 'OPTIONS':
        return response.send('', 204)

    # Load JSON data
    with open(os.path.join(os.path.dirname(__file__), '../data.json')) as f:
        raw_data = json.load(f)

    # Convert list of objects into a name-to-marks dictionary
    data_dict = {entry['name']: entry['marks'] for entry in raw_data}

    # Parse query parameters
    query = parse_qs(request.query_string.decode())
    names = query.get('name', [])

    # Look up marks for each name
    marks = [data_dict.get(name, None) for name in names]

    return response.json({"marks": marks})
