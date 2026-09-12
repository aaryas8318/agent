import os
import re
import urllib.parse

from .contacts import lookup_contact


KEYWORDS = (
    "gmail", "email", "e-mail", "mail",
    "write an email", "send an email", "draft an email",
    "compose an email", "write mail", "send mail", "draft mail",
    "compose mail"
)

def is_email_command(text):
    text = text.lower()
    return any(k in text for k in KEYWORDS)

def extract_email(text):
    """
    Returns (email, label).

    label is a human-friendly description of the recipient, suitable
    for showing in the UI (e.g. "John (john@example.com)"). email is
    the bare address, used to build the Gmail compose URL.
    """

    match = re.search(r"[\w.+-]+@[\w.-]+\.\w+", text)
    if match:
        email = match.group(0)
        return email, email

    match = re.search(
        r"([\w.+-]+)\s+at\s+([\w.-]+)\s+dot\s+(\w+)",
        text.lower()
    )
    if match:
        email = f"{match.group(1)}@{match.group(2)}.{match.group(3)}"
        return email, email

    name, email = lookup_contact(text)
    if email:
        return email, f"{name.capitalize()} ({email})"

    return "", ""

def create_gmail_url(subject="", body="", recipient=""):
    params = urllib.parse.urlencode({
        "view": "cm",
        "fs": "1",
        "to": recipient,
        "su": subject,
        "body": body
    })
    return f"https://mail.google.com/mail/u/0/?{params}"
