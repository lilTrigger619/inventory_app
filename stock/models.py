from django.db import models

# Create your models here.
class Stock_category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Shelve(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class StockItem(models.Model):
    name = models.CharField(max_length=225, blank=False)
    model = models.CharField(max_length=225, blank=True)
    quantity = models.IntegerField(blank=True, default=0)
    cost_price = models.DecimalField(
        blank=True, null=True, decimal_places=2, max_digits=7, default=0.0
    )
    sale_price = models.DecimalField(
        blank=True, null=True, decimal_places=2, max_digits=7, default=0.0
    )
    last_restock = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Stock_category, on_delete=models.CASCADE, related_name="items"
    )
    shelve = models.ForeignKey(Shelve, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# report (name_of_customer, number, reason, date, item)
