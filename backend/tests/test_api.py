import requests
from PIL import Image
from datetime import datetime

BASE_URL = 'http://127.0.0.1:5000'


def test_api_health():
    url = BASE_URL + '/health'
    result = requests.get(url)
    print(result.json())


def test_crud():
    # convert png to bytestring
    url = BASE_URL + '/image_samples'
    
    image = Image.open('backend/tests/example.png')

    payload = dict(
        image_content=image.tobytes().hex(),
        bbox_x=0.1,
        bbox_y=0.1,
        bbox_width=0.1,
        bbox_height=0.1,
        label='cat'
    )
    
    result = requests.post(url, json=payload)
    print(result)
