import json

def handler(request, response):
    import os
    from urllib.parse import parse_qs

    # Enable CORS
    response.headers['Access-Control-Allow-Origin'] = '*'

    # Load marks.json
    with open(os.path.join(os.path.dirname(__file__), '../marks.json')) as f:
        data = json.load(f)

    # Parse query parameters
    query = parse_qs(request.query_string.decode())
    names = query.get('name', [])

    # Look up marks
    marks = [data.get(name, None) for name in names]

    return response.json({"marks": marks})
