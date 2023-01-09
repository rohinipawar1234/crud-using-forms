from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.TextField(default='')
    content=models.TextField(default='')
    date=models.DateField()
    img_1=models.ImageField()


    def __str__(self):
        return self.title
