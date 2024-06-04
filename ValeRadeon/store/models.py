from django.db import models

from ecom.settings import AUTH_USER_MODEL

# Create your models here.

class Product(models.Model) :
    name = models.CharField(max_length=180)
    slug = models.SlugField(max_length=180)
    price = models.FloatField(default=0.0)
    qte = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products-images",blank=True,null=True)
    
    def __str__(self) -> str:
        return f"{self.name} - {self.price}$"


class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qte = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True,null=True)

    # price = models.FloatField(default=0.0)
    # date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.product.name} - {self.qte}$"

class Cart(models.Model):

    # totale 
    
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)


    def __str__(self):
        return self.user.username