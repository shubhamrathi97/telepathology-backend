from rest_framework import generics, viewsets, filters
import django_filters
from .models import *


class SampleView(generics.ListCreateAPIView):
    serializer_class = SampleSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    search_fields = ['patient__name', 'patient__mobile']
    filterset_fields = ('sample_type','patient','patient__name','patient__mobile','operator_id', 'created',
                        'sample_reviews__doctor_id')
    ordering_fields = '__all__'
    ordering = ['created']

    def get_queryset(self):
        queryset = Sample.objects
        reviewed = self.request.query_params.get('reviewed',None)
        if reviewed:
            queryset = Sample.objects.filter(sample_reviews__isnull=not bool(reviewed.lower() == 'true')).distinct()
        if self.request.user.type == 'operator':
            queryset = queryset.filter(operator_id=self.request.user.id)
        return queryset.all()


class SampleReviewed(generics.ListAPIView):
    serializer_class = SampleSerializer
    # queryset = Sample.objects.all()
    queryset = Sample.objects.filter(sample_reviews__isnull=True).all()


class SampleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class SampleReviewView(generics.ListCreateAPIView):
    serializer_class = SampleReviewSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    search_fields = ['sample_id__patient__name', 'sample_id__patient__mobile', 'doctor_id__name', 'doctor_id__mobile']
    filterset_fields = ('sample_id','doctor_id','images_unclear','again_review','sample_id__operator_id')
    ordering_fields = '__all__'
    ordering = ['created']

    def get_queryset(self):
        queryset = SampleReview.objects
        doctor = self.request.query_params.get('doctor',None)
        if doctor and self.request.user.type == 'doctor':
            queryset = queryset.filter(doctor_id=self.request.user.id)
        return queryset.all()

class SampleReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SampleReview.objects.all()
    serializer_class = SampleReviewSerializer


class SampleCommentView(generics.ListCreateAPIView):
    queryset = SampleComment.objects.all()
    serializer_class = SampleCommentSerializer


class SampleCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SampleComment.objects.all()
    serializer_class = SampleCommentSerializer
