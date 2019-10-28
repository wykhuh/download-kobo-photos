import requests
import json
from settings import kobo_api, token

# ====================================
# methods
# ====================================


def fetch_projects():
    response = requests.get(
        kobo_api,
        headers={'Authorization': 'TOKEN ' + token},
        params={'format': 'json'}
    )
    return (response.json()['results'])


def jprint(json_obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(json_obj, indent=4)
    print(text)

# ====================================
# code
# ====================================


projects = fetch_projects()


jprint(projects)
