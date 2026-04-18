import json
import os
import re
from django.conf import settings
import openai

openai.api_key = settings.OPENAI_API_KEY

PROMPT_TEMPLATE = (
    "Act as an SEO expert for internal linking. Analyze the following blog content and suggest 5 to 10 smart internal linking opportunities. "
    "For each suggestion, return a JSON object with keys: anchor_text, suggested_link_topic, placement, reason. "
    "Use natural anchor text, avoid keyword stuffing, and keep the recommendations user-focused and contextual. "
    "Do not add unrelated suggestions. The placement field should explain paragraph and sentence location. "
    "Respond with only a JSON array."
)


def _extract_json(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        matches = re.findall(r"(\[.*\])", text, re.DOTALL)
        for match in matches:
            try:
                return json.loads(match)
            except json.JSONDecodeError:
                continue
    raise


def analyze_internal_links(blog_content, target_keywords="", max_suggestions=8):
    prompt = f"{PROMPT_TEMPLATE}\n\nContent:\n{blog_content}\n\nTarget Keywords: {target_keywords}\n"

    if not settings.OPENAI_API_KEY:
        return _local_fallback(blog_content, target_keywords)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert SEO content strategist."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=900,
        )
        raw = response.choices[0].message.content.strip()
        suggestions = _extract_json(raw)
    except Exception:
        suggestions = _local_fallback(blog_content, target_keywords)

    if isinstance(suggestions, list):
        return suggestions[:max_suggestions]
    return []


def _local_fallback(blog_content, target_keywords):
    paragraphs = [p.strip() for p in blog_content.split("\n\n") if p.strip()]
    suggestions = []
    for idx, paragraph in enumerate(paragraphs[:5], start=1):
        sentence = paragraph.split(". ")[:1][0]
        suggestions.append({
            "anchor_text": sentence[:45].strip() + "...",
            "suggested_link_topic": "Related topic to improve relevance",
            "placement": f"Paragraph {idx}, first sentence",
            "reason": "This passage appears central to the article topic and can reinforce topical authority.",
        })
    return suggestions


def create_highlighted_html(blog_content, suggestions):
    paragraphs = blog_content.split("\n\n")
    highlighted = []
    for paragraph in paragraphs:
        paragraph_html = paragraph
        for suggestion in suggestions:
            anchor = suggestion.get("anchor_text", "")
            if anchor and anchor in paragraph_html:
                paragraph_html = paragraph_html.replace(anchor, f"<mark>{anchor}</mark>")
        highlighted.append(paragraph_html)
    return "<br><br>".join(highlighted)
