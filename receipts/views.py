from django.shortcuts import render
from receipts.models import Receipt

# Create your views here.


def home(request):
    receipt_list = Receipt.objects.all()
    context = {
        "home": receipt_list,
    }
    return render(request, "receipt/home.html", context)
