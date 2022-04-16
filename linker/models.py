from django.db import models

# Create your models here.


class LinkModel(models.Model):
    name = models.CharField(max_length=25)
    lid = models.CharField(max_length=50, primary_key=True)
    target = models.URLField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    wait = models.IntegerField(default=5)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
