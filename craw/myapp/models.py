from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=20)
    card_image = models.URLField(null=True)
    fee = models.TextField(null=True)
    card_type = models.TextField(null=True)
    card_record = models.TextField(null=True)

class Benefit(models.Model):
    benefit_name = models.CharField(max_length=20)
    benefit_content = models.TextField(null=True)
    benefit_detail = models.TextField(null=True)
    card = models.ForeignKey(Data, on_delete=models.CASCADE)
