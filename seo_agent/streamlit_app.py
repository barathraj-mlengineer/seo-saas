import streamlit as st
from pipeline import run_pipeline
from distributor import save_to_pdf, send_email

st.set_page_config(page_title="Autonomous SEO & Marketing AI", layout="wide")
st.title("🤖 Autonomous SEO & Marketing AI Agent")

topic = st.text_input("Enter a topic for content generation", placeholder="e.g. AI in Digital Marketing")

if st.button("Generate Content"):
    if topic:
        with st.spinner("Running pipeline..."):
            result = run_pipeline(topic)
            save_to_pdf(topic, result["blog"], result["image_url"])

        st.success("✅ Content Generated Successfully!")

        st.subheader("📝 Blog Content")
        st.write(result["blog"])

        st.subheader("🔖 Meta Tags")
        st.json(result["meta"])

        st.subheader("📱 Social Media Posts")
        st.json(result["posts"])

        st.subheader("🖼️ Relevant Image")
        st.image(result["image_url"], width=600)

        with open("output.pdf", "rb") as file:
            st.download_button(label="📥 Download Blog as PDF", data=file, file_name="output.pdf")

        st.subheader("📤 Send Email")
        to_email = st.text_input("Recipient Email", value="client@example.com")
        if st.button("Send Email"):
            send_email(to_email, f"New SEO Blog: {topic}", "Blog attached.", "output.pdf")
            st.success("📧 Email sent successfully!")

    else:
        st.warning("⚠️ Please enter a topic first.")
