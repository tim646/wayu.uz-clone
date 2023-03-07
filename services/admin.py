from django.contrib import admin

from .models import ELibraryBook, Categories, ForVolunteers, Partnership, GratuitousHelpText
# Register your models here.

admin.site.register(ELibraryBook)
admin.site.register(Categories)
admin.site.register(Partnership)
admin.site.register(ForVolunteers)
admin.site.register(GratuitousHelpText)
