import cv2
import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np

img_path = 'colour.jpg'
img = cv2.imread(img_path)

index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

# Streamlit app
st.title("Color Detection App")

st.image(img, channels="BGR", caption="Uploaded Image")

x = st.number_input("X coordinate", min_value=0, max_value=img.shape[1] - 1, step=1)
y = st.number_input("Y coordinate", min_value=0, max_value=img.shape[0] - 1, step=1)

if st.button("Detect Color"):
    b, g, r = img[y, x]
    color_name = get_color_name(r, g, b)
    st.write(f"Color at ({x}, {y}): {color_name}")
    st.write(f"RGB values: R={r}, G={g}, B={b}")

    img_copy = img.copy()
    cv2.rectangle(img_copy, (20, 20), (750, 60), (int(b), int(g), int(r)), -1)
    text = f"{color_name} R={r} G={g} B={b}"
    cv2.putText(img_copy, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    if r + g + b >= 600:
        cv2.putText(img_copy, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    st.image(img_copy, channels="BGR", caption="Image with detected color")

