import streamlit as st

import random 
a = random.randint(1,10)
st.write(a)
num = st.text_input("Hello, Please enter a number and I will print all  umbers less than it..")
num = int(num)


for i in range(0,num):
            st.write(i)

from PIL import Image
import io

st.title("Image Uploader")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image data from the UploadedFile object
    bytes_data = uploaded_file.getvalue()

    # Open the image using Pillow (PIL)
    image = Image.open(io.BytesIO(bytes_data))

    st.image(image, caption="Uploaded Image", use_column_width=True)

    # You can now perform further processing on the 'image' object (Pillow Image object)
    st.write("Image uploaded successfully!")
    # Example: Get image dimensions
    st.write(f"Image dimensions: {image.width}x{image.height}")


st.title("Test App")
st.header("numbers")
st.subheader("ai club")
st.write("I love AIclub")
            
