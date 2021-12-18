from django.db import models
from django.conf import settings
from django.core.validators import (
            MinValueValidator,
            MaxValueValidator,
            )
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="movie/")
    actors = models.ManyToManyField(Actor,related_name="actors")
    categories = models.ManyToManyField(Category,related_name="movies")
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    # returns avg rating number
    @property
    def rating(self):
        ratings = self.ratings.all()
        total = 0
        for rate in ratings:
            total += rate.number
        return total / ratings.count()


    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    number = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name="ratings")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'movie'],name="movie-user")
            ]
    def __str__(self):
        return f"{self.user}'s rate"
