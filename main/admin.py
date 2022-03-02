from django.contrib import admin

from . import models

admin.site.register(models.BlogArticle)
admin.site.register(models.FeedbackContact)
admin.site.register(models.WorkExample)
