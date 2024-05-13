import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO

st.title('Background Remover')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    image = uploaded_file.read()
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Processing...")
    output_image = remove(image)
    img_io = BytesIO(output_image)
    img_io.seek(0)
    st.image(img_io, caption='Image without background.', use_column_width=True)
    st.download_button(
        label="Download image with background removed",
        data=img_io.getvalue(),
        file_name='image_no_bg.png',
        mime='image/png'
    )
