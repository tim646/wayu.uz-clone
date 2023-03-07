from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from about.models import BaseModel
from ckeditor.fields import RichTextField

import datetime


class Categories(models.Model):
    category = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.category


current_year = datetime.datetime.now().year


class ELibraryBook(BaseModel):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=90)
    language = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    year_of_publication = models.IntegerField(default=1, validators=[
            MinLengthValidator(1), MaxLengthValidator(int(current_year))
        ]
    )
    num_of_pages = models.PositiveIntegerField(default=0, validators=[MaxLengthValidator(10000)])
    book_file = models.FileField(upload_to='static/assets/book_files')

    def __str__(self):
        return self.title


class ForVolunteers(models.Model):
    body = RichTextField()


class Partnership(models.Model):
    body = RichTextField()


class GratuitousHelpText(models.Model):
    body = RichTextField()
