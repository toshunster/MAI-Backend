from django.db import models

class Product(models.Model):
    title = models.TextField(verbose_name="Продукт", null=False)
    price = models.IntegerField(verbose_name="Цена", null=False)

    def __str__(self):
        return f"{self.title} - {self.price} рублей"
