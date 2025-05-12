from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    pub_date = models.DateTimeField()
    weather = models.CharField(max_length=10)
    image = models.ImageField(upload_to="post/", blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:20]