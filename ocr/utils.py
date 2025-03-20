import re
import os
import easyocr
import cv2
import numpy as np
from PIL import Image

# Initialize EasyOCR Reader
reader = easyocr.Reader(['en'])

def preprocess_image(image_path):
    """Preprocess the image to improve OCR accuracy."""
    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)


    cv2.imwrite("processed_image.jpg", gray)
    os.remove("processed_image.jpg")
    return gray

def extract_text_from_image(image_path):
    img=preprocess_image(image_path)
    """Extract text from an image using EasyOCR."""
    result = reader.readtext(img, detail=0)
    return " ".join(result)

def extract_dates_from_aadhar(image_path):
    text = extract_text_from_image(image_path)
    print(text)
    dob_pattern = r"\b(\d{2}[-/.]\d{2}[-/.]\d{4})\b"

    dob_match = re.findall(dob_pattern, text)
    dob_list=[]
    for dob in dob_match:
        dob_list.append(dob)

    return {
        "Date of Birth": dob_list if dob_match else "Not Found"
    }