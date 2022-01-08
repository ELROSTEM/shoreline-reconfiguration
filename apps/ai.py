import cv2
import numpy as np
import streamlit as st


def app():

    st.title("AI stuff")
    st.write("do some ai stuff")
    st.write("if you are doing this part you are a god and you are really just too smart so you dont even need to care about coding cause you are literally machine learning engineer pls teach me.")

    ## Read
    img = cv2.imread(r"https://raw.githubusercontent.com/ELROSTEM/shoreline-reconfiguration/main/photos/sunflower.jpg")


    ## convert to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    ## mask of green (36,25,25) ~ (86, 255,255)
    # mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
    mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))

    ## slice the green
    imask = mask>0
    green = np.zeros_like(img, np.uint8)
    green[imask] = img[imask]

    ## save 
    cv2.imwrite("green.png", green)


    st.image(img, use_column_width=True, clamp= True)
    st.image(green, use_column_width=True,clamp = True)

