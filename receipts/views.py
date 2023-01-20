from django.shortcuts import render, redirect
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm


# Create your views here.


@login_required
def home(request):
    receipt_list = Receipt.objects.filter(purchaser=request.user)
    context = {
        "home": receipt_list,
    }
    return render(request, "receipt/home.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()
    context = {"form": form}
    return render(request, "receipt/create.html", context)
