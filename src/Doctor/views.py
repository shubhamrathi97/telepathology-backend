from rest_framework import generics, filters
from rest_framework.response import Response
import django_filters
from .models import Doctor, DoctorSerializer
from backend import permissions


class DoctorRegisterView(generics.CreateAPIView):
    permission_classes = ()
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DoctorListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdmin,)

    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    search_fields = ['name', 'mobile','id']
    filterset_fields = ('id', 'mobile', 'name')
    ordering_fields = '__all__'



class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdmin,)

    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

    def update(self, request, *args, **kwargs):
        partial = True  # Here I change partial to True
        instance = self.get_object()
        data = request.data.copy()
        data.pop('password', None)
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)