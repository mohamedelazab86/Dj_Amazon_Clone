from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
# create  data base  
class Product(models.Model):
    flag_types=[
        ('New','New'),
        ('Sale','SaLE'),
        ('Feature','Feature'),
                ]
    name=models.CharField(max_length=120,verbose_name=_('name'))
    flag=models.CharField(max_length=100,choices=flag_types)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    
