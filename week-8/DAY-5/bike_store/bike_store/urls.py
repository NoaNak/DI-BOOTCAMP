from django.contrib import admin
from django.urls import path
from bike.views import customers, customer, add_customer, Rental_list, rent_detail, vehicle_list, vehicle_detail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("customers/", customers),
    path("customer/<int:id>", customer),
    path("add_customer/", add_customer),
    path("Rental_list/", Rental_list),
    path("rent_detail/<int:pk>/", rent_detail),
    path("vehicle_list/", vehicle_list), 
    path("vehicle_detail/", vehicle_detail)
]

