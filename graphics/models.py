from django.db import models

class Graphic(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='graphics/images/')
    

    def __str__(self):
        return self.title