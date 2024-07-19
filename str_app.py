from flask import Flask, request, send_file, render_template
from rembg import remove
from PIL import Image
from io import BytesIO
import os

app = Flask(__name__, static_folder='src/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file and allowed_file(file.filename):
        image = file.read()
        output_image = remove(image)
        
        img = Image.open(BytesIO(output_image)).convert("RGBA")
        img_io = BytesIO()
        img.save(img_io, 'PNG', quality=70)  
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='image_transparent_bg.png')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['jpg', 'png']

if __name__ == '__main__':
    app.run(debug=False)  