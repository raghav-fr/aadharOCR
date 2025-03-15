import cv2
import pytesseract
import re
import numpy as np
from PIL import Image


def preprocess_image(image_path):
    """Preprocess the image to improve OCR accuracy."""
    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 11, 2)

    cv2.imwrite("processed_image.jpg", gray)

    return gray

def extract_dates_from_aadhar(image_path):
    """Extracts DOB and Issue Date from Aadhaar card image."""
    processed_img = preprocess_image(image_path)

    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(processed_img, config=custom_config, lang="eng")

    print("Extracted Text:\n", text)

    date_pattern = r'\b(\d{2}[-/]\d{2}[-/]\d{4})\b'
    dates = re.findall(date_pattern, text)

    dob, issue_date = None, None

    for match in dates:
        if "DOB" in text or "Birth" in text or "Date of Birth" in text:
            dob = match
        elif "Issue" in text or "Issued" in text:
            issue_date = match

    if len(dates) == 2 and not dob and not issue_date:
        dob, issue_date = dates

    return {"dob": dob or "DOB not found", "issue_date": issue_date or "Issue Date not found"}
