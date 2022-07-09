from xml.etree.ElementTree import Comment
from django.db import models

# Create your models here.
class TikiNgonItem(models.Model):
    ItemID = models.AutoField(primary_key=True)
    Name = models.CharField()
    Price = models.FloatField()
    Discount = models.IntegerField()
    Stars = models.FloatField()
    NumStarts = models.IntegerField()
    ImageItem = models.ImageField()
    NumBuys = models.IntegerField()
    InStock = models.IntegerField()
    Provider = models.CharField()
    Amount = models.IntegerField()
    Description = models.CharField()