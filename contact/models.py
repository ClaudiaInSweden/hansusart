from django.db import models

# Create your models here.
class Contact(models.Model):

    class Meta:
        ordering = ['-date']

    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True)
    topic = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(max_length=1000,null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    answered = models.BooleanField(default=False)

    def __str__(self):
        return f'Message {self.message} from {self.email} topic {self.topic}'