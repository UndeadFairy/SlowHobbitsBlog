from django.db import models
from django.utils import timezone


class Post1(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    upload = models.ImageField(upload_to='', default = 'kitten.jpg')
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
