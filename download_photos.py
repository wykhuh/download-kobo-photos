import requests
import json
import os

from settings import token, kobo_api, media_url

# ====================================
# methods
# ====================================


def fetch_projects():
    response = requests.get(
        kobo_api,
        headers={'Authorization': 'TOKEN ' + token},
        params={'format': 'json'}
    )

    if response.status_code == 200:
        return (response.json()['results'])
    else:
        print('Could not fetch assets')
        return None


def fetch_submissions(project_url):
    response = requests.get(
        project_url,
        headers={'Authorization': 'TOKEN ' + token},
        params={'format': 'json'}
    )

    if response.status_code == 200:
        return (response.json()['results'])
    else:
        print('Could not fetch submissions')
        return None


def jprint(json_obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(json_obj, indent=4)
    print(text)


def download_file(directory_name, file_url):
    # https://www.codementor.io/aviaryan/downloading-files-from-urls-in-python-77q3bs0un
    filename = file_url.rsplit('/', 1)[1]
    response = requests.get(url, headers={'Authorization': 'TOKEN ' + token})

    if not os.path.exists('photos'):
        os.mkdir('photos')
    if not os.path.exists(f"photos/{directory_name}"):
        os.mkdir(f"photos/{directory_name}")

    open(f"photos/{directory_name}/{filename}", 'wb').write(response.content)

# ====================================
# code
# ====================================


projects = fetch_projects()
if not projects:
    continue

for project in projects:
    url = project['data']
    submissions = fetch_submissions(url)
    if not submissions:
        continue

    for submission in submissions:
        directory = str(submission['_id'])
        photos = submission['_attachments']

        for photo in photos:
            url = f"{media_url}{photo['filename']}"
            download_file(directory, url)
