from django.shortcuts import render
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def home(request):
    receipt_list = Receipt.objects.filter(purchaser=request.user)
    context = {
        "home": receipt_list,
    }
    return render(request, "receipt/home.html", context)
