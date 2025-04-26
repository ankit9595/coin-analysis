from django.db import models

# Create your models here.
class Comparision(models.Model):
    image_name = models.CharField(max_length=252, null=True)
    currency = models.CharField(max_length=252, null=True)
    country = models.CharField(max_length=252, null=True)
    coin_rupee_value = models.CharField(max_length=252, null=True)
    coin_year = models.CharField(max_length=4, null=True)
    coin_mint_marks = models.CharField(max_length=252, null=True)
    coin_mint_marks_city= models.CharField(max_length=252, null=True)
    color= models.CharField(max_length=252, null=True)
    shape= models.CharField(max_length=252, null=True)
    which_metal_body= models.CharField(max_length=252, null=True)
    coin_symbol= models.CharField(max_length=252, null=True)
    reverse_symbol= models.CharField(max_length=252, null=True)
    weight= models.CharField(null=True, max_length=50)
    size= models.CharField(null=True, max_length=50)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    price = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.image_name}"
 
# class Coin(models.Model):
#     currency = models.CharField(max_length=100, blank=True)
#     country = models.CharField(max_length=100, blank=True)
#     coin_rupee_value = models.CharField(max_length=50, blank=True)
#     coin_year = models.CharField(max_length=50, blank=True)
#     coin_mint_marks_city = models.CharField(max_length=100, blank=True)
#     shape = models.CharField(max_length=100, blank=True)
#     metal_body = models.CharField(max_length=100, blank=True)
#     price = models.CharField(max_length=100, blank=True)

#     def __str__(self):
#         return f"{self.currency} - {self.coin_year}"
