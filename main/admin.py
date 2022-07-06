from django.contrib import admin

from . import models

admin.site.register(models.BlogArticle)
admin.site.register(models.FeedbackContact)
admin.site.register(models.WorkExample)
admin.site.register(models.Service)
admin.site.register(models.FAQuestion)

@admin.register(models.Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ("group", "slug", "value")
    list_filter = ("group", )