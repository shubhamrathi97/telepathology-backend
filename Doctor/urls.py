from django.urls import path

from . import views

urlpatterns = [
    path('', views.DoctorListView.as_view()),
    path('<int:pk>/', views.DoctorDetailView.as_view()),
    path('register/', views.DoctorRegisterView.as_view())
]