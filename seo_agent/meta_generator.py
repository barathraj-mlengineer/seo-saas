def generate_meta(title, blog_text):
    return {
        "meta_title": f"{title} | AI Content",
        "meta_description": blog_text[:150],
        "keywords": ", ".join(title.lower().split())
    }
