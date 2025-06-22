from apscheduler.schedulers.blocking import BlockingScheduler
from pipeline import run_pipeline
from distributor import save_to_pdf, send_email
import datetime

def scheduled_run():
    topic = "AI in Ecommerce"
    result = run_pipeline(topic)
    save_to_pdf(topic, result["blog"], result["image_url"])
    send_email("client@email.com", f"New SEO Blog: {topic}", "Blog attached.", "output.pdf")
    print(f"[{datetime.datetime.now()}] SEO Pipeline executed.")

scheduler = BlockingScheduler()
scheduler.add_job(scheduled_run, 'interval', days=1)
scheduler.start()
