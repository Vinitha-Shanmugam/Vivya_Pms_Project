from django.contrib.auth.hashers import make_password
from datetime import date
from dateutil.relativedelta import relativedelta
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.utils.crypto import get_random_string
from VivyaPms_app.models import VivyapmsAppAuthtoken, Users
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from rest_framework.generics import GenericAPIView
import pandas as pd
from django.utils import timezone
from . import models
from . import serializers
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
import logging


class UserDetailsPost(GenericAPIView):
    serializer_class = serializers.UserSerializer

    def post(self, request, **kwargs):
        try:
            query = models.Users.objects.filter(email=request.data['email'])
            serializer_class = serializers.UserdetailsSerializer(query, many=True)
            logging.info("User data has been fetched Successfully.")
            data = {
                'response_code': 200,
                'message': 'User details fetched successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_class.data
            }
            return Response(data)
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'User details fetching failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str(e),
                'data': []
            }
            logging.error("User details Fetching process is failed.")
            return Response(data)


class UserDetailsGet(GenericAPIView):
    serializer_class = serializers.UserSerializer

    def get(self, request, **kwargs):
        try:
            query = models.Users.objects.filter(email=kwargs['email'])
            serializer_class = serializers.UserdetailsSerializer(query, many=True)
            logging.info("User data has been fetched Successfully.")
            data = {
                'response_code': 200,
                'message': 'User details fetched successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_class.data
            }
            return Response(data)
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'User details fetching failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str(e),
                'data': []
            }
            logging.error("User details Fetching process is failed.")
            return Response(data)


class UserDetailsCreate(GenericAPIView):
    serializer_class = serializers.UserCreateSerializer

    def post(self, request, **kwargs):
        try:
            serializer_class = serializers.UserCreateSerializer(data=request.data)
            if serializer_class.is_valid():
                hashed_password = make_password(serializer_class.validated_data['password'])
                serializer_class.validated_data['password'] = hashed_password
                if serializer_class.validated_data['valid_option'].lower() == 'yearly':
                    serializer_class.validated_data['end_date'] = date.today() + relativedelta(years=1)
                elif serializer_class.validated_data['valid_option'].lower() == 'half yearly':
                    serializer_class.validated_data['end_date'] = date.today() + relativedelta(months=6)
                elif serializer_class.validated_data['valid_option'].lower() == 'quarterly':
                    serializer_class.validated_data['end_date'] = date.today() + relativedelta(months=3)
                serializer_class.save()
            logging.info("User data has been posted Successfully.")
            data = {
                'response_code': 200,
                'message': 'User details posted successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_class.data
            }
            return Response(data)
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'User details posting failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str(e),
                'data': []
            }
            logging.error("User details posting process is failed.")
            return Response(data)


class RoomTypeGetAll(GenericAPIView):
    serializer_class = serializers.AddRoomTypeSerializer

    def get(self, request, *args, **kwargs):
        try:

            queryset = models.RoomType.objects.all()
            serializer = serializers.AddRoomTypeSerializer(queryset, many=True)

            # Return the serialized data
            data = {
                'response_code': 200,
                'message': 'Room types fetched successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer.data
            }
            return Response(data)
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'Room types fetching failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str(e),
                'data': []
            }
            logging.error("Room types fetching process failed.")
            return Response(data)


class RoomTypeGet(GenericAPIView):
    serializer_class = serializers.AddRoomTypeSerializer

    def get(self, request, room_type_id, *args, **kwargs):
        try:
            data = models.RoomType.objects.get(
                room_type_id=room_type_id)

            serializer = serializers.AddRoomTypeSerializer(data)
            logging.info("User data has been fetched Successfully.")
            data = {
                'response_code': 200,
                'message': 'User details fetched successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer.data
            }
            return Response(data)
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'User details fetching failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str(e),
                'data': []
            }
            logging.error("User details fetching process is failed.")
            return Response(data)


class UpdateRoomType(UpdateAPIView):
    serializer_class = serializers.UpdateRoomTypeSerializer

    def put(self, request, *args, **kwargs):
        try:
            data = models.RoomType.objects.get(room_type_id=request.data['room_type_id'])
            serializer_instance = serializers.AddRoomTypeSerializer(instance=data, data=request.data)
            serializer_instance.is_valid(raise_exception=True)
            self.perform_update(serializer_instance)
            logging.info("User data has been updated Successfully.")
            data = {
                'response_code': 200,
                'message': 'User details updated successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_instance.data
            }
            return Response(data)
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'User details updating failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str(e),
                'data': []
            }
            logging.error("User details updating process is failed.")
            return Response(data)


class UpdateRoom(UpdateAPIView):
    serializer_class = serializers.UpdateRoomSerializer

    def put(self, request, *args, **kwargs):
        try:
            data = models.Room.objects.get(room_id=request.data['room_id'])
            serializer_instance = serializers.AddRoomSerializer(instance=data, data=request.data)
            serializer_instance.is_valid(raise_exception=True)
            self.perform_update(serializer_instance)
            logging.info("User data has been updated Successfully.")
            data = {
                'response_code': 200,
                'message': 'Room details updated successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_instance.data
            }
            return Response(data)
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'Room details updating failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str(e),
                'data': []
            }
            logging.error("Room details updating process is failed.")
            return Response(data)


class DeleteRecordsView(GenericAPIView):
    serializer_class = serializers.DeleteSerializer

    def post(self, request, *args, **kwargs):
        try:
            room_type_id = request.data.get('room_type_id')
            models.Room.objects.filter(room_type_id=room_type_id).delete()
            models.RoomType.objects.filter(room_type_id=room_type_id).delete()
            return JsonResponse({'message': 'Records deleted successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class Login(GenericAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = Users.objects.get(email=email)

            if check_password(password, user.password):
                user_token = self.get_or_generate_user_token(user)
                account_status = self.get_account_status(user)

                response_data = {
                    "response_code": 200,
                    "Status flag": True,
                    "token": user_token,
                    "user": {
                        "user_id": user.user_id,
                        "first_name": user.first_name,
                        "email_id": user.email
                    },
                    "Account_status": account_status
                }

                return JsonResponse(response_data, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        except Users.DoesNotExist:
            return JsonResponse({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def get_or_generate_user_token(self, user):
        token = VivyapmsAppAuthtoken.objects.filter(user_id=user.user_id).first()

        if not token:
            token = VivyapmsAppAuthtoken.objects.create(
                digest=get_random_string(128),
                token_key=get_random_string(8),
                created=timezone.now(),
                user_id=user.user_id
            )

        return token.token_key

    def get_account_status(self, user):
        if user.user_type == "super-admin":
            return "S"
        elif user.user_type == "admin" and date.today() < user.end_date:
            return "A"
        elif user.user_type == "user":
            return "U"
        else:
            return "Unknown"


@parser_classes([MultiPartParser])
class ExcelFileUploadView(GenericAPIView):
    serializer_class = serializers.ExcelFileUploadSerializer

    def post(self, request, format=None):
        serializer = serializers.ExcelFileUploadSerializer(data=request.data)

        if serializer.is_valid():
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)
            for index, row in df.iterrows():
                try:
                    property_name = row['Property name']
                    name = row['Room type']
                    property_objects = models.Property.objects.filter(name=property_name)
                    print(property_objects)
                    for property_obj in property_objects:
                        room_type_objects = models.RoomType.objects.filter(name=name)
                        print(room_type_objects)
                        if room_type_objects.count() == 1:
                            room_type_id = room_type_objects.first().room_type_id
                        elif room_type_objects.count() > 1:
                            print("Multiple room type objects with the same name. Skipping row.")
                            continue
                        else:
                            print("No RoomType object with the specified name. Skipping row.")
                            continue
                    print(room_type_id)

                    models.Room.objects.create(
                        admin_id=serializer.validated_data['admin_id'],
                        property_id=property_obj.property_id,
                        name=row['Room number'],
                        room_occupaied_status=row['Availability'],
                        room_type_id=room_type_id,
                        is_active=row['Status'],
                        created_at=timezone.now(),
                    )

                except Exception as e:
                    print(f"Error processing row {index}: {e}")

            return Response({'message': 'Data imported successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryTableGetAll(GenericAPIView):

    def get(self, request, *args, **kwargs):
        try:

            query = models.Country.objects.all()
            serializer = serializers.CountryTableSerializer(query, many=True)

            # Return the serialized data
            data = {
                'response_code': 200,
                'message': 'Country details fetched successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer.data
            }
            return Response(data)
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'Country details fetching failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str(e),
                'data': []
            }
            logging.error("Country details fetching process failed.")
            return Response(data)


class PurposeToVisitGetAll(GenericAPIView):

    def get(self, request, *args, **kwargs):
        try:

            query = models.PurposeToVisit.objects.all()
            serializer = serializers.PurposeToVisitSerializer(query, many=True)

            data = {
                'response_code': 200,
                'message': 'Purpose to visit details fetched successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer.data
            }
            return Response(data)
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'Purpose to visit details fetching failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str(e),
                'data': []
            }
            logging.error("Purpose to visit details fetching process failed.")
            return Response(data)


# @parser_classes([MultiPartParser])
class PropertyDetailsCreate(GenericAPIView):
    serializer_class = serializers.PropertySerializer

    def post(self, request, **kwargs):
        try:
            serializer_class = serializers.PropertySerializer(data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
            logging.info("Property details has been posted Successfully.")
            data = {
                'response_code': 200,
                'message': 'Property details posted successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_class.data
            }
            return Response(data)
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'Property details posting failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str(e),
                'data': []
            }
            logging.error("Property details posting process is failed.")
            return Response(data)


class UpdatePropertyDetails(UpdateAPIView):
    serializer_class = serializers.PropertyUpdateSerializer

    def put(self, request, *args, **kwargs):
        try:
            data = models.Property.objects.get(property_id=request.data['property_id'])
            serializer_instance = serializers.PropertySerializer(instance=data, data=request.data)
            serializer_instance.is_valid(raise_exception=True)
            self.perform_update(serializer_instance)
            logging.info("Property details has been updated Successfully.")
            data = {
                'response_code': 200,
                'message': 'Property details updated successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_instance.data
            }
            return Response(data)
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'Property details updating failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str(e),
                'data': []
            }
            logging.error("Property details updating process is failed.")
            return Response(data)


class UpdatePurposeToVisit(UpdateAPIView):
    serializer_class = serializers.PurposeToVisitUpdateSerializer

    def put(self, request, *args, **kwargs):
        try:
            data = models.PurposeToVisit.objects.get(id=request.data['id'])
            serializer_instance = serializers.PurposeToVisitSerializer(instance=data, data=request.data)
            serializer_instance.is_valid(raise_exception=True)
            self.perform_update(serializer_instance)
            logging.info("Purpose To Visit details has been updated Successfully.")
            data = {
                'response_code': 200,
                'message': 'Purpose To Visit  details updated successfully',
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': serializer_instance.data
            }
            return Response(data)
        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'Purpose To Visit  details updating failed',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str(e),
                'data': []
            }
            logging.error("Purpose To Visit  details updating process is failed.")
            return Response(data)
