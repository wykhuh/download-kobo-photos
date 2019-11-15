# Download Kobo Toolbox Photos

A script to download photos from [Kobo Toolbox](https://www.kobotoolbox.org).

This script calls the Kobo API to get a list of all the projects, and makes
another API call to get submissions for a project. It will download all the photos
for each submission and create a CSV with data about each photo.

## Instructions

1. Install the dependencies using either `requirements_conda.txt` or
   `requirements_pip.txt`

2. rename `settings.example.py` to `settings.py` and fill in the values.

3. run `python download_photos.py`
