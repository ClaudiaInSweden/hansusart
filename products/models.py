from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=254, blank=False, null=False)
    width = models.CharField(max_length=254, blank=False, null=False)
    height = models.CharField(max_length=254, blank=False, null=False)
    description = models.CharField(max_length=254, blank=False, null=False)
    highlight = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)
    image = models.ImageField(blank=False, null=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)