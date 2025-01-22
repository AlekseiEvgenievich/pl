from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Seller(models.Model):  # Исправлено с model.Model на models.Model
    # Связь один-к-одному с пользователем
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="seller")

    @property
    def published_ads_count(self):
        return self.ad_set.count()


class Category(models.Model):
    name = models.SlugField(default="", null=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ad(models.Model):  # Исправлено с model.Model на models.Model
    name = models.CharField(max_length=255)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
