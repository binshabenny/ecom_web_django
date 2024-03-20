from django.db import models

#  models for products here.
class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES =((LIVE ,'live'),(DELETE,'delete'))
    title = models.CharField(max_length=200)
    price = models.FloatField(max_length=200)
    original_price = models.FloatField(max_length=200)
    description  = models.TextField(max_length = 250)
    image = models.ImageField(upload_to='products/')
    priority = models.IntegerField(default = 0)
    delete_status = models.IntegerField(choices= DELETE_CHOICES,default=LIVE)
    created_at =models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now =True)

    def __str__(self) -> str:
        return self.title

