from pipeline import run_pipeline

if __name__ == "__main__":
    topic = input("Enter topic for SEO campaign: ")
    result = run_pipeline(topic)
    print("--- Blog ---\n", result["blog"])
    print("\n--- Meta Tags ---\n", result["meta"])
    print("\n--- Social Posts ---\n", result["posts"])
    print("\n--- Image URL ---\n", result["image_url"])
