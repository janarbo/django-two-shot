from django.urls import path
from receipts.views import home


urlpatterns = [
    path("", home, name="home"),
]
