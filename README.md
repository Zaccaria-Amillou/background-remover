# Background Image Remover

This is a simple Streamlit application that allows users to upload an image and remove its background.

## Features
- Upload an image (supports .jpg and .png formats)
- Display the uploaded image
- Process the image to remove the background
- Downloads the results directly
## Installation

To install the necessary dependencies be sure to run the following command

```bash
pip install -r requirements.txt
```

## Usage

To start the Streamlit app, navigate to the project directory and run the following commang:

```bash
python str_app.py
```

Then, open your web browse and go http://127.0.0.1:5000 to view the app.

## Unit Test
If you'd like to run a test to see if everything is functional you can type

```bash
 pytest unit_test.py
```

## Example

<table>
  <tr>
    <td align="center">
      <img src="src/static/img/before.png" width="200" style="border:1px solid black">
      <br />
      <em>Before</em>
    </td>
    <td align="center">
      <img src="src/static/img/after.png" width="200" style="border:1px solid black">
      <br />
      <em>After</em>
    </td>
  </tr>
</table>