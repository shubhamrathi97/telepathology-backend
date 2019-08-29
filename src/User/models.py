from django.db import models
from Address.models import Address
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.postgres.fields import JSONField
from rest_framework import serializers
import datetime
from rest_auth.registration.serializers import RegisterSerializer
from django.utils import timezone

# Create your models here.
gender_choice = (('M','male'),('F','female'),('O','other'))

class Meta:
   ordering = ['-id']


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, mobile, password, type, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        address = extra_fields.pop('address', None)
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            type=type,
            mobile=mobile,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        if address:
            address = Address.objects.create(**address)
            user.address = address
        user.save(using=self._db)
        return user

    def create_user(self, email, mobile, password, type='user', **extra_fields):
        return self._create_user(email, mobile, password, type, False, False, **extra_fields)

    def create_staffuser(self, email, mobile, password, type='admin', **extra_fields):
        return self._create_user(email, mobile, password, type, True, False, **extra_fields)

    def create_superuser(self, email, mobile, password, type='admin', **extra_fields):
        return self._create_user(email, mobile, password, type, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    mobile = models.CharField(max_length=20, unique=True)
    gender = models.CharField(choices=gender_choice, null=True, max_length=15)
    dob = models.DateField(null=True, default=datetime.date.today)
    type = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.DO_NOTHING, blank=True, null=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        indexes = [
            models.Index(fields=['email'], name='email_idx'),
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('password','groups','user_permissions',)


class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(required=True)
    dob = serializers.DateField(required=False)
    mobile = serializers.CharField(required=True)
    gender = serializers.CharField(required=False)
    type = serializers.CharField(required=False)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
                'password': self.validated_data.get('password', ''),
                'email': self.validated_data.get('email', ''),
                'name': self.validated_data.get('name', ''),
                'dob': self.validated_data.get('dob', ''),
                'mobile': self.validated_data.get('mobile', ''),
                'gender': self.validated_data.get('gender', ''),
                'type': self.validated_data.get('type', ''),
        }


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','name','dob','mobile','gender','type')
        read_only_fields = ('id','email','mobile')
