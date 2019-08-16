from django.db import models
from backend.models import BaseModel
from rest_framework import serializers

class Address(BaseModel):
    address_line_1 = models.TextField(null=True)
    address_line_2 = models.TextField(null=True)
    address_line_3 = models.TextField(null=True)
    pincode = models.TextField(null=True)
    city = models.TextField(null=True)
    state = models.TextField(null=True)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'