from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def generate_blog(topic, keywords):
    prompt = f"""Write an SEO-optimized blog post about "{topic}".
Use keywords: {', '.join(keywords)}. Ensure it's engaging and informative (500+ words)."""

    res = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content
