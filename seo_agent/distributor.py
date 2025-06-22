from fpdf import FPDF
import os
import smtplib
from email.message import EmailMessage

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", size=16)
        self.cell(200, 10, txt="SEO Report", ln=True, align="C")

def save_to_pdf(title, blog, image_url=None, path="output.pdf"):
    pdf = PDF()

    pdf.set_font("Helvetica", size=14)
    pdf.add_page()
    pdf.cell(200, 10, txt=title, ln=True)
    pdf.ln(5)
    pdf.multi_cell(0, 10, blog)

    pdf.output(path)

def send_email(to_email, subject, body, attachment="output.pdf"):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "sbarathraj.ai@gmail.com"
    msg["To"] = to_email
    msg.set_content(body)

    with open(attachment, "rb") as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=attachment)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("sbarathraj.ai@gmail.com", "abi@12345")
        smtp.send_message(msg)

