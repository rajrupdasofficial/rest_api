from django.db import models

# Create your models here.

class Product(models.Model):
    title=models.CharField(max_length=120)
    content=models.TextField(blank=True, null=True)
    price=models.DecimalField(max_digits=15,decimal_places=2,default=99.99)

    def __self__(self):
        return f"title of the product is-- (self.title)"
    """ Django class property for sale price tag with floating point claculation"""
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)
    """to calculate write Product.obejcts.last().price or sale_price"""
    def get_discount(self):
        return "500"
