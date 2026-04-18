from django import forms


class ContentAnalysisForm(forms.Form):
    blog_content = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 12,
            "placeholder": "Paste your blog article here...",
        }),
        label="Blog Content",
        help_text="Paste full blog content for analysis.",
    )
    target_keywords = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Optional keywords, comma separated",
        }),
        label="Target Keywords",
        help_text="Optional: comma-separated seed keywords for SEO focus.",
    )