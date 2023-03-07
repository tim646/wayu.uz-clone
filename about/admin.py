from django.contrib import admin

from .models import Hashtag, News, Events, MigrationLaw, InstagramPost, UsefulLinks, YouNeedToKnow
# Register your models here.
admin.site.register(Hashtag)
admin.site.register(News)
admin.site.register(Events)
admin.site.register(MigrationLaw)
admin.site.register(InstagramPost)
admin.site.register(YouNeedToKnow)
admin.site.register(UsefulLinks)

