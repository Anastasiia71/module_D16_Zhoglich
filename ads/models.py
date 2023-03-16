from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Ad(models.Model):

    CATEGORIES = (
        ('tank', 'танк'),
        ('healer', 'хилер'),
        ('dd', 'ДД'),
        ('merchant', 'торговец'),
        ('guild-master', 'гильдиастер'),
        ('questioner', 'квестгивер'),
        ('blacksmith', 'кузнец'),
        ('tanner', 'кожевник'),
        ('potion-master', 'зельевар'),
        ('spell-master', 'мастер заклинаний'),
    )
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    content = models.TextField()
    category = models.CharField(max_length=13, choices=CATEGORIES, default='merchant')
    upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f'{self.title}: {self.content:20}'

    def get_absolute_url(self):
        return reverse('ad_detail', args=[str(self.id)])

    def preview(self):
        return self.content[0:123] + '...'


class Response(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author}: {self.text}'

    def get_absolute_url(self):
        return reverse('response_detail', args=[str(self.id)])
