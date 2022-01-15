

import cv2
import numpy as np
import streamlit as st
from PIL import Image


def app():

    st.title("AI for Costal Shoreline")


    st.header("Algae Detection")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            Algae is an informal term for a large and diverse group of photosynthetic eukaryotic organisms. It is a polyphyletic grouping that includes species from multiple distinct clades. Included organisms range from unicellular microalgae, such as Chlorella, Prototheca and the diatoms, to multicellular forms, such as the giant kelp, a large brown alga which may grow up to 50 metres in length.
            No definition of algae is generally accepted. One definition is that algae "have chlorophyll as their primary photosynthetic pigment and lack a sterile covering of cells around their reproductive cells".[3] Likewise, the colorless Prototheca under Chlorophyta are all devoid of any chlorophyll. Although cyanobacteria are often referred to as "blue-green algae", most authorities exclude all prokaryotes from the definition of algae.[4][5] Algae constitute a polyphyletic group[4] since they do not include a common ancestor, and although their plastids seem to have a single origin, from cyanobacteria,[6] they were acquired in different ways. Green algae are examples of algae that have primary chloroplasts derived from endosymbiotic cyanobacteria. Diatoms and brown algae are examples of algae with secondary chloroplasts derived from an endosymbiotic red alga.[7] Algae exhibit a wide range of reproductive strategies, from simple asexual cell division to complex forms of sexual reproduction.[8]
        """)
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/NSW_seabed_1.JPG/330px-NSW_seabed_1.JPG")
        st.caption("Sea dikes are onshore structures with the principal function of protecting low-lying areas against flooding. Sea dikes are usually built as a mound of fine materials like sand and clay with a gentle seaward slope in order to reduce the wave runup and the erodible effect of the waves. The surface of the dike is armored with grass, asphalt, stones, or concrete slabs (USACE, 2005).")


    #Take Picture
    picture = st.camera_input("Take a picture")
    if picture:
        # Save Image
        img = Image.open(picture)
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


    #Upload Image
    img = st.file_uploader("Upload an image")
    st.caption(""" Please click on the image uploader. If you are on IOS you can simply select the take photo option. If you are on PC please upload
    a folder from your file explorer""")
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

