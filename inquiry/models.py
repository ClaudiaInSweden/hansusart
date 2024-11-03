from django.db import models
from products.models import Product
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Inquiry(models.Model):

    class Meta:
        verbose_name_plural = 'Inquiries'
        ordering = ['-date']

    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    street1 = models.CharField(max_length=255, null=True, blank=True)
    street2 = models.CharField(max_length=255, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(max_length=1000,null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    answered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Konstverk {self.product} Name {self.first_name} {self.last_name} Date {self.date}'