# Generated by Django 4.2.5 on 2023-09-16 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Stock_category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="StockItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=225)),
                ("model", models.CharField(blank=True, max_length=225)),
                ("quantity", models.IntegerField(blank=True, default=0)),
                (
                    "stock_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0.0, max_digits=7
                    ),
                ),
                (
                    "sale_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0.0, max_digits=7
                    ),
                ),
                ("last_restock", models.DateTimeField(auto_now=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="stock.stock_category",
                    ),
                ),
            ],
        ),
    ]
