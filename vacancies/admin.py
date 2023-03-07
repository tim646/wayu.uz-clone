from django.contrib import admin

from .models import Volunteer, Vacancy, Resume, InternShip
# Register your models here.

admin.site.register(Volunteer)
admin.site.register(Vacancy)
admin.site.register(Resume)
admin.site.register(InternShip)
