import requests
import json
import sys

def getData(url):
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(json.dumps(response.json()))
    else:
        print(f'Error: {response.json()}')
        sys.exit()
