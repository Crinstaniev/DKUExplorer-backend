import base64
from datetime import datetime
from io import BytesIO

import requests
from PIL import Image

BASE_URL = 'http://127.0.0.1:5000'


def test_api_health():
    url = BASE_URL + '/health'
    result = requests.get(url)
    print(result.json())


def test_crud():
    # convert png to bytestring
    url = BASE_URL + '/image_samples'

    # open image
    image = Image.open('backend/tests/example.png')
    # convert to base64 string
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = str(base64.b64encode(buffered.getvalue()))

    payload = dict(
        image_content=img_str,
        bbox_x=0.1,
        bbox_y=0.1,
        bbox_width=0.1,
        bbox_height=0.1,
        label='cat'
    )

    result = requests.post(url, json=payload)
    print(result)
