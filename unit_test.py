import os
import pytest
from str_app import app
from werkzeug.datastructures import FileStorage
from io import BytesIO

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_upload_file(client):
    # Open the actual image file in binary mode
    with open('src/static/img/before.png', 'rb') as img_file:
        data = {
            'file': (img_file, 'before.png')
        }
        # Send POST request to /upload route
        response = client.post('/upload', content_type='multipart/form-data', data=data)
    
    # Assert the response status code
    assert response.status_code == 200
    # Optionally, assert other aspects of the response (e.g., content type, attachment filename)
    assert response.content_type == 'image/png'
    assert 'image_transparent_bg.png' in response.headers.get('Content-Disposition')