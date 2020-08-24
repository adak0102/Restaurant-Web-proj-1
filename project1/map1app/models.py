from django.db import models

# Create your models here.
class Maps(models.Model) :
    locate_x=models.FloatField(null=True)
    locate_y=models.FloatField(null=True)
    res_name=models.CharField(max_length=18, null=True)
    res_type=models.CharField(max_length=10, null=True)
