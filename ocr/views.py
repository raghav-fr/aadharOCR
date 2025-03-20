from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import extract_dates_from_aadhar
import os
from django.shortcuts import render
import json
from pdf2image import convert_from_path
import requests
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


@api_view(['POST'])
def extract_dates_api(request):
    if 'aadhar_image' not in request.FILES:
        return Response({"error": "No file uploaded"}, status=400)

    image = request.FILES["aadhar_image"]
    temp_path = "uploaded_aadhar.jpg"

    with open(temp_path, "wb") as f:
        f.write(image.read())

    extracted_dates = extract_dates_from_aadhar(temp_path)

    os.remove(temp_path)

    return Response(extracted_dates)

def upload_page(request):
    return render(request, "ocr/upload.html")


def convert_pdf_to_image(pdf_path):
    images = convert_from_path(pdf_path, poppler_path="C:/Users/user/Downloads/poppler-24.08.0/Library/bin" if os.name == "nt" else None)
    if images:
        image_path = pdf_path.replace(".pdf", ".jpg")  
        images[0].save(image_path, "JPEG")  
        return image_path
    return None

def upload_and_redirect(request):
    if request.method == "POST" and request.FILES.get("aadhar_file"):
        uploaded_file = request.FILES["aadhar_file"]
        file_extension = uploaded_file.name.lower().split('.')[-1]

        temp_path = default_storage.save(f"temp_aadhar.{file_extension}", ContentFile(uploaded_file.read()))

        if file_extension == "pdf":
            tem_path=temp_path
            temp_path = convert_pdf_to_image(default_storage.path(tem_path))
            os.remove(tem_path)

        if not temp_path:
            return render(request, "ocr/results.html", {"json_data": json.dumps({'error': 'Invalid file format'}, indent=4)})

        api_url = "http://127.0.0.1:8000/api/extract_dates/"
        with open(default_storage.path(temp_path), "rb") as file:
            response = requests.post(api_url, files={"aadhar_image": file})

        default_storage.delete(temp_path)

        json_data = json.dumps(response.json(), indent=4) if response.status_code == 200 else json.dumps({'error': 'OCR failed'}, indent=4)
        return render(request, "ocr/results.html", {"json_data": json_data})

    return redirect("upload_page")
