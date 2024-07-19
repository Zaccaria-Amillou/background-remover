import pytest
from unittest.mock import patch
from PIL import Image
from io import BytesIO
from str_app import remove_background

def create_test_image_bytes():
    img = Image.new('RGB', (100, 100), color = 'red')
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    return img_bytes.read()

@pytest.fixture
def image_bytes():
    return create_test_image_bytes()

@patch('str_app.remove')
def test_remove_background(mock_remove, image_bytes):
    # Mock the remove function to return the original image bytes
    mock_remove.return_value = image_bytes

    result_img = remove_background(image_bytes)

    assert isinstance(result_img, Image.Image), "The result should be an instance of PIL.Image.Image"
    assert result_img.mode == "RGBA", "The image mode should be RGBA for transparency"