import json
from django.shortcuts import render
from .forms import ContentAnalysisForm
from .models import AnalysisHistory
from .utils import analyze_internal_links, create_highlighted_html


def analyze(request):
    suggestions = []
    highlighted_html = ""
    export_text = ""
    if request.method == "POST":
        form = ContentAnalysisForm(request.POST)
        if form.is_valid():
            blog_content = form.cleaned_data["blog_content"].strip()
            target_keywords = form.cleaned_data["target_keywords"].strip()
            suggestions = analyze_internal_links(blog_content, target_keywords)
            highlighted_html = create_highlighted_html(blog_content, suggestions)
            export_lines = []
            for idx, item in enumerate(suggestions, start=1):
                export_lines.append(f"Suggestion {idx}:")
                export_lines.append(f"Anchor Text: {item.get('anchor_text')}")
                export_lines.append(f"Suggested Link Topic: {item.get('suggested_link_topic')}")
                export_lines.append(f"Placement: {item.get('placement')}")
                export_lines.append(f"Reason: {item.get('reason')}")
                export_lines.append("")
            export_text = "\n".join(export_lines)
            AnalysisHistory.objects.create(
                blog_content=blog_content,
                target_keywords=target_keywords,
                suggestions_json=json.dumps(suggestions, ensure_ascii=False),
            )
    else:
        form = ContentAnalysisForm()

    return render(request, "seo/index.html", {
        "form": form,
        "suggestions": suggestions,
        "highlighted_html": highlighted_html,
        "export_text": export_text,
    })
