# Django OCR Project

This project is a Django-based web application that extracts dates (Date of Birth and Issue Date) from Aadhaar card images and PDFs using OCR (Optical Character Recognition).

## Features
- **Image & PDF Upload**: Supports both image and PDF formats.
- **OCR Processing**: Extracts Date of Birth (DOB) and Issue Date.
- **JSON Response**: Displays extracted data in a new page.
- **File Handling**: Uses a dedicated `/upload/` directory for processing files.

---

## Installation & Setup

### 1 **Clone the Repository**
```bash
git clone https://github.com/raghav-fr/aadharOCR.git
cd aadharOCR
```

### 2 **Create a Virtual Environment** (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3 **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4 **Install Poppler (Required for PDF Processing)**
#### **Windows**:
- Download Poppler: [https://github.com/oschwartz10612/poppler-windows/releases](https://github.com/oschwartz10612/poppler-windows/releases)
- Extract it (e.g., `C:\poppler-23.11.0`)
- Add `C:\poppler-23.11.0\bin` to **System Environment Variables > Path**
- Change the poopler path in \ocr\views.py in convert_pdf_to_image()

### 5 **Run the Server**
```bash
python manage.py runserver
```

Now, visit: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** to access the upload page.

---

## **Usage**
1. **Upload an Image or PDF** containing an Aadhaar card.
2. **OCR extracts DOB & Issue Date** automatically.
3. **JSON results** will be displayed on a new page.

---

## **API Endpoints**
| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET` | `/` | Redirects to `/upload/` |
| `GET` | `/upload/` | Upload page |
| `POST` | `/upload/process_upload/` | Extracts dates and returns JSON |

---
