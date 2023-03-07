from django.db import models
from about.models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField

JOB_TYPE_CHOICES = [
    ('fullTime', 'FullTime'),
    ('PartTime', 'PartTime'),
    ("Contract", "Contract"),
    ("Other", "Other")
]

REGION_CHOICES = [
    ("Toshkent", "Toshkent"),
    ("Xorazm", "Xorazm"),
    ("Navoiy", 'Navoiy'),
    ("Farg'ona", "Farg'ona"),
    ("Samarqand", "Samarqand"),
    ("Buxoro", "Buxoro"),
    ("Andijon", "Andijon")
]

FIELD_OF_STUDY = [
        ('CS', 'Computer Science'),
        ('BS', 'Business'),
    ]
UNIVERSITIES = [
    ('WIUT', 'Westminister'),
    ('IUT', 'Inha'),
    ('TDYU', 'Toshkent Davlat Yuridik Universiteti'),
        ]


class Vacancy(BaseModel):
    job_title = models.CharField(max_length=90)
    description = RichTextField()
    min_salary = models.DecimalField(default=0, max_digits=11, decimal_places=2)
    max_salary = models.DecimalField(default=0, max_digits=11, decimal_places=2)
    job_type = models.CharField(max_length=25, choices=JOB_TYPE_CHOICES)
    phone_number = PhoneNumberField()
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.job_title


class Resume(BaseModel):
    vacancy_obj = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='vacancy_obj')
    phone_number = PhoneNumberField()
    resume_file = models.FileField()

    def __str__(self):
        return self.vacancy_obj


class Volunteer(BaseModel):
    full_name = models.CharField(max_length=70)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    resume_file = models.FileField()

    def __str__(self):
        return self.full_name


class InternShip(Volunteer):
    date_of_birth = models.DateField(verbose_name="Tugilgan sana: dd/mm/yyyy")
    region = models.CharField(max_length=40, choices=REGION_CHOICES)
    job_field = models.CharField(max_length=70)
    desired_start_date = models.DateField(verbose_name="Desired Internship start date")
    job_type_intern = models.CharField(max_length=30, choices=JOB_TYPE_CHOICES)
    job_type_after_internship = models.CharField(max_length=30, choices=JOB_TYPE_CHOICES)
    university = models.CharField(max_length=80, choices=UNIVERSITIES, null=True)
    faculty = models.CharField(max_length=80, choices=FIELD_OF_STUDY)
    start_date_of_study = models.DateField()
    end_date_of_study = models.DateField()
    gpa = models.DecimalField(default=0, decimal_places=2, max_digits=4)
    experience = models.TextField(blank=True)
    skills = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.full_name} - {self.job_field}"


