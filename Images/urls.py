from django.urls import path
from . import views

urlpatterns = [
    path('get_upload_url/',views.GetUploadURL.as_view()),
    path('set_upload_public/',views.SetURLPublic.as_view()),
    path('upload_image/', views.UploadImage.as_view())
]