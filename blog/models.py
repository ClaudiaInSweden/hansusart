from django.db import models
from django.urls import reverse
from datetime import datetime, date


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Blog(models.Model):

    STATUS = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )

    title = models.CharField(max_length=254)
    intro = models.TextField()
    text = models.TextField()
    status = models.CharField(choices=STATUS, default='Draft', max_length=254)
    image = models.ImageField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    highlight = models.BooleanField(default=False)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.date} - {self.status} - {self.category} : {self.title}'

    class Meta:
        ordering = ('-date',)