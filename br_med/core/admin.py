from django.contrib import admin

from br_med.core.models import Quote


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ["date", "currency", "value"]
