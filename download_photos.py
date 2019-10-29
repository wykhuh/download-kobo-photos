import requests
import json
import os
import csv
from PIL import Image
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
        print('Could not fetch submissions: ', project_url)
        return None


def jprint(json_obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(json_obj, indent=4)
    print(text)


def download_file(directory_name, file_url):
    photo_dir = 'kobo_photos'
    # https://www.codementor.io/aviaryan/downloading-files-from-urls-in-python-77q3bs0un
    filename = file_url.rsplit('/', 1)[1]
    response = requests.get(url, headers={'Authorization': 'TOKEN ' + token})

    if not os.path.exists(photo_dir):
        os.mkdir(photo_dir)

    if not os.path.exists(f"{photo_dir}/{directory_name}"):
        os.mkdir(f"{photo_dir}/{directory_name}")

    path = f"{photo_dir}/{directory_name}/{filename}"

    open(path, 'wb').write(response.content)
    return path


def find_image_dimensions(path):
    im = Image.open(path)
    width, height = im.size
    return {'width': width, 'height': height}

# ====================================
# code
# ====================================


header = ['submission_id', 'source_filename',
          'filename', 'path', 'width', 'height', 'payload']

projects = fetch_projects()
if not projects:
    exit()

with open('kobo_photos.csv', 'wt') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)

    for project in projects:
        url = project['data']
        submissions = fetch_submissions(url)
        if not submissions:
            continue

        for submission in submissions:
            directory = str(submission['_id'])
            photos = submission['_attachments']

            for photo in photos:
                url = f'{media_url}{photo["filename"]}'
                path = download_file(directory, url)
                dim = find_image_dimensions(path)

                row = [
                    submission['_id'],
                    photo["filename"],
                    file,
                    path,
                    dim['width'],
                    dim['height'],
                    photo
                ]
                csv_writer.writerow(row)
