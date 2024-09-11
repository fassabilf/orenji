from django.db import models

class OrenjiEntry(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    descriptions = models.TextField()
    stock = models.IntegerField()
    
    @property
    def is_can_buy(self):
        return self.stock > 0