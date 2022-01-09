

import cv2
import numpy as np
import streamlit as st
from PIL import Image


def create_opencv_image_from_stringio(img_stream, cv2_img_flag=0):
    img_stream.seek(0)
    img_array = np.asarray(bytearray(img_stream.read()), dtype=np.uint8)
    return cv2.imdecode(img_array, cv2_img_flag)

def get_opencv_img_from_buffer(buffer, flags):
    bytes_as_np_array = np.frombuffer(buffer.read(), dtype=np.uint8)
    return cv2.imdecode(bytes_as_np_array, flags)

def app():

    st.title("AI stuff")
    st.write("do some ai stuff")
    st.write("if you are doing this part you are a god and you are really just too smart so you dont even need to care about coding cause you are literally machine learning engineer pls teach me.")
    

    #Upload Image
    img = st.file_uploader("Upload an image")
    if img is not None:

        # Save Image
        img = Image.open(img)
        img = img.save("img.jpg")

        # Read Image
        img = cv2.imread("img.jpg")

        ## convert to hsv
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        ## mask of green (36,25,25) ~ (86, 255,255)
        mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))

        ## slice the green
        imask = mask>0
        green = np.zeros_like(img, np.uint8)
        green[imask] = img[imask]

        ## save 
        cv2.imwrite("green.png", green)


        st.image(img, use_column_width=True, clamp= True)
        st.image(green, use_column_width=True,clamp = True)

