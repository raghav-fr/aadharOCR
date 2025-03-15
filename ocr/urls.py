from django.urls import path
from .views import extract_dates_api, upload_page ,upload_and_redirect

urlpatterns = [
    path("extract_dates/", extract_dates_api, name="extract_dates_api"),
    path("upload/", upload_page, name="upload_page"),
    path("process_upload/", upload_and_redirect, name="upload_and_redirect"),
]
