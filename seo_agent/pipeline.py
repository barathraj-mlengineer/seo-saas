from keyword_tool import get_keywords
from content_writer import generate_blog
from meta_generator import generate_meta
from social_post import generate_social_posts
from image_fetcher import get_image_url

def run_pipeline(topic):
    keywords = get_keywords(topic)
    blog = generate_blog(topic, keywords)
    meta = generate_meta(topic, blog)
    posts = generate_social_posts(blog, topic)
    image_url = get_image_url(topic)

    return {
        "topic": topic,
        "keywords": keywords,
        "blog": blog,
        "meta": meta,
        "posts": posts,
        "image_url": image_url
    }
