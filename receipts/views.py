from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm, ExpenseCategoryForm


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


@login_required
def category_list(request):
    category = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "categories": category,
    }
    return render(request, "receipt/categories.html", context)


@login_required
def account_list(request):
    account = Account.objects.filter(owner=request.user)
    context = {"accounts": account}
    return render(request, "receipt/accounts.html", context)


@login_required
def create_category(request):
    if request.method == "POST":
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(False)
            category.owner = request.user
            category.save()
            return redirect("category_list")
    else:
        form = ExpenseCategoryForm()
    context = {"form": form}
    return render(request, "receipt/category_create.html", context)
