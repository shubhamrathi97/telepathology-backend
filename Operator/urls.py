from django.urls import path
from . import views

urlpatterns = [
    path('', views.OperatorList.as_view()),
    path('<int:pk>/',views.OperatorDetail.as_view()),
    path('register/', views.OperatorRegister.as_view())
]