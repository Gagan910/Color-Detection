import cv2
import pandas as pd
import streamlit as st
import numpy as np

img_path = r's:\Projects\Color-detection-main\Color-detection-main\colour.jpg'
img = cv2.imread(img_path)

if img is None:
    st.error(f"Failed to load image from path: {img_path}")
    st.stop()

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

index = ["color", "color_name", "hex", "R", "G", "B"]
csv_path = r's:\Projects\Color-detection-main\Color-detection-main\colors.csv'
try:
    csv = pd.read_csv(csv_path, names=index, header=None)
except FileNotFoundError:
    st.error(f"CSV file not found at path: {csv_path}")
    st.stop()

def get_color_name(R, G, B):
    minimum = 10000
    cname = ""
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

st.title("Color Detection App")

st.image(img_rgb, caption="Uploaded Image", use_column_width=True)

x = st.number_input("X coordinate", min_value=0, max_value=img.shape[1] - 1, step=1)
y = st.number_input("Y coordinate", min_value=0, max_value=img.shape[0] - 1, step=1)

if st.button("Detect Color"):
    b, g, r = img[y, x]
    color_name = get_color_name(r, g, b)
    st.write(f"Color at ({x}, {y}): {color_name}")
    st.write(f"RGB values: R={r}, G={g}, B={b}")

    img_copy = img_rgb.copy()
    cv2.rectangle(img_copy, (20, 20), (750, 60), (int(b), int(g), int(r)), -1)
    text = f"{color_name} R={r} G={g} B={b}"
    cv2.putText(img_copy, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    if r + g + b >= 600:
        cv2.putText(img_copy, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    st.image(img_copy, caption="Image with detected color", use_column_width=True)
