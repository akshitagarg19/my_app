import json

def handler(request):
    try:
        with open("marks.json", "r") as f:
            data = json.load(f)
        
        # Extract names from query string
        names = request.query.getlist("name")
        
        # Fetch marks for each name
        results = [data.get(name, 0) for name in names]

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            },
            "body": json.dumps({ "marks": results })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
