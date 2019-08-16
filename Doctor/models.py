from django.db import models
from User.models import User, PermissionsMixin
from rest_framework import serializers


class Doctor(User, PermissionsMixin):
    degree = models.TextField(null=True)


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        # fields= '__all__'
        exclude = ('groups', 'user_permissions','is_superuser','is_staff')

    def create(self, validated_data):
        validated_data['type'] = 'doctor'
        res = Doctor.objects.create_user(**validated_data)
        return res

    def to_representation(self, obj):
        rep = super(DoctorSerializer, self).to_representation(obj)
        rep.pop('password', None)
        return rep
