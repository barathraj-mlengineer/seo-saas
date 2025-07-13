from fpdf import FPDF
import smtplib
from email.message import EmailMessage


class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        self.set_font("Helvetica", "", 14)  # ✅ using built-in font

    def header(self):
        self.set_font("Helvetica", "", 16)
        self.cell(200, 10, txt="SEO Report", ln=True, align="C")
        self.ln(10)


def save_to_pdf(title, blog, image_url=None, path="output.pdf"):
    pdf = PDF()
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

    # ⚠️ WARNING: This is hardcoded and insecure. Use environment variables in production!
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("sbarathraj.ai@gmail.com", "abi@12345")  # ← Replace with app password
        smtp.send_message(msg)
