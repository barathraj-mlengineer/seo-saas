def generate_social_posts(blog_text, topic):
    short = blog_text[:220]
    return {
        "linkedin": f"🚀 New Post: {topic}\n{short}...\nRead more at [your link] #SEO #AI",
        "twitter": f"{topic}: {short[:240]}..."
    }
