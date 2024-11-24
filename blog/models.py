from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Blog(models.Model):

    STATUS = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )


    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=254)
    intro = models.TextField()
    text = models.TextField()
    status = models.CharField(choices=STATUS, default='Draft', max_length=254)
    image = models.ImageField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    highlight = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.date} - {self.status} - {self.categories} : {self.title}'

    class Meta:
        ordering = ('-date',)