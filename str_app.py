import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO

def allowed_file(filename):
    return '.' in filename and filename.split('.', 1)[1].lower() in ['jpg', 'png']

def remove_background(image_bytes):
    output_image = remove(image_bytes)
    img = Image.open(BytesIO(output_image)).convert("RGBA")
    return img

st.title('Background Remover')

uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png'])
if uploaded_file is not None:
    if allowed_file(uploaded_file.name):
        bytes_data = uploaded_file.getvalue()
        st.image(bytes_data, caption='Original Image', use_column_width=True)
        
        result_img = remove_background(bytes_data)
        
        st.image(result_img, caption='Image with Transparent Background', use_column_width=True)
        
        # To let users download the result image
        buf = BytesIO()
        result_img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.download_button(label="Download Image",
                           data=byte_im,
                           file_name="image_transparent_bg.png",
                           mime="image/png")
    else:
        st.error("Unsupported file type. Please upload a JPG or PNG image.")