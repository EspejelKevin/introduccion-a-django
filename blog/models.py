from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.title