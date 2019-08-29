from django.urls import path
from . import views

urlpatterns = [
    path('sample/', views.SampleView.as_view()),
    path('sample/<int:pk>/', views.SampleDetailView.as_view()),
    path('sample_reviewed/', views.SampleReviewed.as_view()),
    path('review/', views.SampleReviewView.as_view()),
    path('review/<int:pk>/', views.SampleReviewDetailView.as_view()),
    path('comment/', views.SampleCommentView.as_view()),
    path('comment/<int:pk>/', views.SampleCommentDetailView.as_view())
]
