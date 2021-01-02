from django.contrib import admin

from adventureProjectSia.advanture_app.models import Article, NewsAndEvents


class NewsAndEventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'place', 'time',)
    list_filter = ('title', 'place', 'time',)


admin.site.register(Article)
admin.site.register(NewsAndEvents, NewsAndEventsAdmin)
