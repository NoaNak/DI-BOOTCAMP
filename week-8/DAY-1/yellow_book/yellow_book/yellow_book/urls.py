from django.contrib import admin
from django.urls import path
from phonenumbers.views import find_by_number, find_by_name

urlpatterns = [
    path("admin/", admin.site.urls),
    path("phonenumber/<str:phonenumber>", find_by_number),
    path("name/<str:name>", find_by_name)
]
