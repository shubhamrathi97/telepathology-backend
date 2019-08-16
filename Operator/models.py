from User.models import User, PermissionsMixin
from rest_framework import serializers


class Operator(User, PermissionsMixin):
    def __str__(self):
        return self.email


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        # fields= '__all__'
        exclude = ('groups', 'user_permissions','is_superuser','is_staff')

    def create(self, validated_data):
        validated_data['type'] = 'operator'
        res = Operator.objects.create_user(**validated_data)
        return res

    def to_representation(self, obj):
        rep = super(OperatorSerializer, self).to_representation(obj)
        rep.pop('password', None)
        return rep
