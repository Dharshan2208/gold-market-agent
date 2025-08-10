import re
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from langchain_core.messages import AIMessage

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))


def clean_llm_output(text: str) -> str:
    """
    Remove markdown stars, hashes, and extra spaces from LLM output.
    """
    text = re.sub(r"[*#`]+", "", text)  # remove *, #, `
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)  # clean multiple blank lines
    return text.strip()


def send_report_email(report_text):
    """
    Sends the gold market report via email in 'Baka' style.
    """
    sender = EMAIL_USER
    recipient = EMAIL_TO
    password = EMAIL_PASS

    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = "Baka --> Here's Your Gold Market Report....Read It, Yaro!"

    formatted_text = (
        f"\nYour Gold Market Analysis\n\n"
        f"{report_text}\n\n"
        f"Regards,\nYour One and Only Baka Bot....Peace Bro"
    )
    message.attach(MIMEText(formatted_text, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, message.as_string())
        server.quit()
        print("Gold Market Report sent to your inbox.")
    except Exception as e:
        print(f"Failed to send email report: {str(e)}")


def formatter_node(state):
    """
    LangGraph node to clean, format, and email the LLM's output.
    """
    last_message = state["messages"][-1]
    if isinstance(last_message, AIMessage):
        cleaned_text = clean_llm_output(last_message.content)
        send_report_email(cleaned_text)
        return {"messages": [AIMessage(content=cleaned_text)]}
    return state
