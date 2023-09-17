from django.urls import path
from .views import index, Inventory_view, add_inventory_view, single_category_view

app_name="stock"

urlpatterns = [
    path("", index, name="dashboard"),
    path("inventory/", Inventory_view, name="inventory"),
    path("add-inventory/", add_inventory_view, name="add-inventory"),
    path("categories/<int:pk>/", single_category_view, name="single-category"),
]
