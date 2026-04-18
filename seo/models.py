from django.db import models


class AnalysisHistory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    blog_content = models.TextField()
    target_keywords = models.CharField(max_length=255, blank=True)
    suggestions_json = models.TextField()

    def __str__(self):
        return f"SEO analysis {self.created_at:%Y-%m-%d %H:%M}"