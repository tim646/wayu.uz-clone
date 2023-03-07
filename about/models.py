from django.db import models
from django.utils.text import slugify
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()


class Hashtag(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class BaseNewsEvents(BaseModel):
    title = models.CharField(max_length=120)
    body = RichTextField()
    slug = models.SlugField(unique=True, blank=True)
    hashtags = models.ManyToManyField(Hashtag)


class News(BaseNewsEvents):
    image = models.ImageField(upload_to="images/news_images/", blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Events(BaseNewsEvents):
    image = models.ImageField(upload_to='images/events_images/', blank=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class MigrationLaw(BaseModel):
    country = CountryField(verbose_name="Country")
    migration_law_file = models.FileField()

    def __str__(self):
        return self.country.name


class InstagramPost(models.Model):
    image_url = models.URLField()
    post_image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)


class UsefulLinks(models.Model):
    image = models.ImageField(upload_to='images/useful_links_images')
    title = models.CharField(max_length=150)
    link = models.URLField()

    def __str__(self):
        return str(self.link)


class YouNeedToKnow(models.Model):
    image = models.ImageField(upload_to='images/useful_links_images')
    body = RichTextField()



