from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from about.models import BaseModel


class FAQ(BaseModel):
    question_title = models.CharField(max_length=150)
    answer = models.TextField()

    def __str__(self):
        return self.question_title


class UserQuestion(BaseModel):
    fullname = models.CharField(max_length=90)
    phone_number = PhoneNumberField()
    question = models.TextField()

    def __str__(self):
        return self.fullname
