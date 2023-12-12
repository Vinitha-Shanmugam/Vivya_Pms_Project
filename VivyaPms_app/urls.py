from VivyaPms import swagger_service
from django.urls import path, include
from . import views

urlpatterns = [

    path('docs/', swagger_service.schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('user/', views.UserDetailsPost.as_view()),
    path('user/str<email>/', views.UserDetailsGet.as_view()),
    path('user/create/', views.UserDetailsCreate.as_view()),
    path('user/login/', views.Login.as_view()),
    path('room_type/update/', views.UpdateRoomType.as_view()),
    path('room_type/get/<int:room_type_id>/', views.RoomTypeGet.as_view()),
    path('room_type/getall/', views.RoomTypeGetAll.as_view()),
    path('room/update/', views.UpdateRoom.as_view()),
    path('upload_excel/', views.ExcelFileUploadView.as_view(), name='upload_excel'),
    path('delete/', views.DeleteRecordsView.as_view(), name="delete/roomtype"),
    path('country_getall/', views.CountryTableGetAll.as_view(), name="getall_country"),
    path('purpose to visit_getall/', views.PurposeToVisitGetAll.as_view(), name="getall_purpose to visit"),
    path('Property_post/', views.PropertyDetailsCreate.as_view(), name="property_details_create"),
    path('Property_update/', views.UpdatePropertyDetails.as_view(), name="property_details_create"),
    path('PurposeToVisit_update/', views.UpdatePurposeToVisit.as_view(), name="property_details_create"),
    # path('api/login/', views.LoginAPIView.as_view(), name='login_api'),
]
