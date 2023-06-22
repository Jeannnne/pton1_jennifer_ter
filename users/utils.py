import os

import requests

from pton1_jennifer_ter import settings


def download_default_profile_image():
    image_url = settings.DEFAULT_IMAGE_LINK
    response = requests.get(image_url)
    response.raise_for_status()

    os.makedirs(settings.DEFAULT_IMAGES_DIR, exist_ok=True)
    default_image_path = os.path.join(settings.DEFAULT_IMAGES_DIR, settings.DEFAULT_IMAGE_NAME)

    with open(default_image_path, 'wb') as f:
        f.write(response.content)
    return settings.DEFAULT_IMAGES_DIR_NAME + '/' + settings.DEFAULT_IMAGE_NAME
