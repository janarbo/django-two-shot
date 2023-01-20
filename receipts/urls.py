from django.urls import path
from receipts.views import home, create_receipt


urlpatterns = [
    path("", home, name="home"),
    path("create/", create_receipt, name="create_receipt")
]
