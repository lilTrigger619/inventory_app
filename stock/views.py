from django.shortcuts import render
from django.views import generic
from .models import Stock_category, StockItem, Shelve

from .forms import Add_inventory_form

# Create your views here.
required_context = {
    "shelves": Shelve.objects.all(),
    "categories": Stock_category.objects.all(),
}


def index(request):
    context = {**required_context}
    print("hello")
    return render(request, "stock/index.html", context)


def Inventory_view(request):
    template_name = "stock/inventory.html"
    return render(request, template_name)


def add_inventory_view(request):
    template = "stock/add-inventory.html"
    if request.method != "POST":
        return render(request, template, {**required_context})
    print("the data", request.POST)
    p_data = Add_inventory_form(request.POST)
    if p_data.is_valid():
        print("the data", p_data.cleaned_data)
        try:
            category = Stock_category.objects.get(pk=p_data.cleaned_data["category"])
            shelve = Shelve.objects.get(pk=p_data.cleaned_data["shelve"])
            data = {**p_data.cleaned_data, "category": category, "shelve": shelve}
            StockItem.objects.create(**data)
        except (Stock_category.DoesNotExist, Shelve.DoesNotExist, Exception) as e:
            print("the error", e)
            return render(
                request,
                template,
                {
                    **required_context,
                    "status": "Invalid data submitted! Try refreshing page.",
                },
            )
        return render(
            request,
            template,
            {**required_context, **p_data.cleaned_data, "status": "200"},
        )
    return render(request, template, {**required_context, "status": p_data.errors})


def single_category_view(request):
    context = {**required_context}
    return render(request, "stock/categories.html", context)
