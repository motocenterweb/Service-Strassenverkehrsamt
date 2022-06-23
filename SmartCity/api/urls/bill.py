from django.urls import path
from rest_framework import routers
from api.views import bill


urlpatterns = [
     path("bill/create", bill.add_bill),
     path("bill/user/", bill.get_bill_by_user)
]