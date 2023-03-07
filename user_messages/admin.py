from django.contrib import admin

from .models import FAQ, UserQuestion
# Register your models here.
admin.site.register(FAQ)
admin.site.register(UserQuestion)
