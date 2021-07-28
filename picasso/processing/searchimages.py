"""
    Search Google images for image matching text tweeted by user

    @author Alex Farrell
"""
from google_images_download import google_images_download
import re


response = google_images_download.googleimagesdownload()


def downloadimages(query):

    arguments = {"keywords": query,
                 "format": "jpg",
                 "limit": 1,
                 "print_urls": True,
                 "silent_mode": True,
                 "no_download": True,
                 "size": "medium",
                 }
    try:
        path = response.download(arguments)


        # Handling File NotFound Error
    except FileNotFoundError:
        arguments = {"keywords": query,
                     "format": "jpg",
                     "limit": 1,
                     "print_urls": False,
                     "size": "medium"}

        # Providing arguments for the searched query
        try:
            # Downloading the photos based
            # on the given arguments
            path = response.download(arguments)
        except:
            pass

    return path


def get_image_url(text_input):
    url = str(downloadimages(text_input))
    extracted_url = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', url)
    for item in extracted_url:
        return item


