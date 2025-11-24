from django.db import models


class Product(models.Model):
    name = models.TextField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True, verbose_name="stock")
    image = models.ImageField(
        upload_to="products/images/", null=True, blank=True, verbose_name="Product Image"
    )

    def __str__(self):
        return self.name
