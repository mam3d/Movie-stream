from django.db import models
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
    actor = models.ManyToManyField(Actor,related_name="actors")
    category = models.ManyToManyField(Category,related_name="movies")
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

