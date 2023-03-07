from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField

from phonenumber_field.modelfields import PhoneNumber
from ckeditor.fields import RichTextField

from about.models import BaseModel


class PersonBase(BaseModel):
    fullname = models.CharField(max_length=80, verbose_name='Person Name')
    phone_num = PhoneNumber()
    job_title = models.CharField(max_length=100)
    email = models.EmailField()
    responsibilities = RichTextField()


class Management(PersonBase):
    biography = RichTextField()
    working_hours_start = models.TimeField(validators=[MinValueValidator('09:00:00'), MaxValueValidator('17:00:00')])
    working_hours_end = models.TimeField(validators=[MinValueValidator('09:00:00'), MaxValueValidator('17:00:00')])

    def __str__(self):
        return self.job_title


class Branches(PersonBase):
    country = CountryField(verbose_name="Country")
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.country.name


