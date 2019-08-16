from django.urls import path

from . import views
from .authorization import CustomAuthToken

urlpatterns = [
    path('', views.UserView.as_view(), name='user_view'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('login/',  CustomAuthToken.as_view())
]