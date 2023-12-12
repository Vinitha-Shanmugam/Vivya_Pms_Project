from django.contrib.auth import authenticate
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = ['email']


class UserdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = ['user_id', 'first_name', 'email', 'phone', 'is_active', 'valid_option', 'end_date', 'user_limit']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = ['user_type', 'user_id', 'first_name', 'email', 'phone', 'is_active', 'valid_option', 'end_date',
                  'user_limit',
                  'last_name', 'password', 'email_verified', 'admin_id', 'status', 'created_at']


class AddRoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoomType
        fields = "__all__"


class AddRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = "__all__"


class UpdateRoomTypeSerializer(serializers.Serializer):
    room_type_id = serializers.IntegerField()
    admin_id = serializers.IntegerField()
    name = serializers.CharField()
    is_active = serializers.CharField()


class UpdateRoomSerializer(serializers.Serializer):
    property_id = serializers.IntegerField()
    room_id = serializers.IntegerField()
    room_type_id = serializers.IntegerField()
    admin_id = serializers.IntegerField()
    name = serializers.CharField()
    is_active = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')


from rest_framework import serializers
from .models import VivyapmsAppAuthtoken


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = VivyapmsAppAuthtoken
        fields = '__all__'


class DeleteSerializer(serializers.Serializer):
    room_type_id = serializers.IntegerField()


class ExcelFileUploadSerializer(serializers.Serializer):
    excel_file = serializers.FileField()
    admin_id = serializers.IntegerField()


class CountryTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = "__all__"


class PurposeToVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PurposeToVisit
        fields = "__all__"


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Property
        fields = "__all__"


class PropertyUpdateSerializer(serializers.Serializer):
    property_id = serializers.IntegerField()
    admin_id = serializers.IntegerField()
    property_type_id = serializers.IntegerField()
    name = serializers.CharField()
    contact_number = serializers.CharField(max_length=50)
    website = serializers.CharField(max_length=255)
    mobile_number = serializers.CharField(max_length=255)
    manager_name = serializers.CharField(max_length=255)
    registration_id = serializers.CharField(max_length=255)
    po_box = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=255)
    pin = serializers.CharField(max_length=10)
    logo = serializers.CharField()
    is_active = serializers.CharField()
    created_at = serializers.CharField()
    created_by = serializers.IntegerField()
    status = serializers.CharField()


class PurposeToVisitUpdateSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name = serializers.CharField()
    is_active = serializers.CharField()
