import re
import os
import easyocr

# Initialize EasyOCR Reader
reader = easyocr.Reader(['en'])

def extract_text_from_image(image_path):
    """Extract text from an image using EasyOCR."""
    result = reader.readtext(image_path, detail=0)
    return " ".join(result)

def extract_dates_from_aadhar(image_path):
    text = extract_text_from_image(image_path)
    print(text)
    dob_pattern = r"\b(\d{2}[-/]\d{2}[-/]\d{4})\b"

    dob_match = re.findall(dob_pattern, text)

    return {
        "Date of Birth": dob_match[0] if dob_match else "Not Found"
    }