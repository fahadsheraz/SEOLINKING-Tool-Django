from django.contrib import admin
from .models import AnalysisHistory


@admin.register(AnalysisHistory)
class AnalysisHistoryAdmin(admin.ModelAdmin):
    list_display = ("created_at", "target_keywords")
    search_fields = ("target_keywords", "blog_content")
    readonly_fields = ("created_at",)
