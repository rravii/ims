from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()

    class Meta:
        db_table = "products"
