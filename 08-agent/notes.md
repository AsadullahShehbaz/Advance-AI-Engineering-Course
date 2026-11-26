# Adding an Email Tool

**Goal:** give the agent one tool, `send_email`, that sends real emails via Gmail SMTP.

## 1. Get a Gmail App Password

Enable 2-Step Verification, then create a password at https://myaccount.google.com/apppasswords. Copy the 16 characters without spaces.

## 2. Add credentials to `.env`

```
GROQ_API_KEY=your_groq_api_key
SMTP_USER=your_email@gmail.com
SMTP_APP_PASSWORD=your16charpassword
```

Add `.env` to `.gitignore`.

## 3. Write the tool

```python
import os, smtplib
from email.message import EmailMessage
from langchain.tools import tool

@tool
def send_email(to: str, subject: str, body: str) -> str:
    """Send an email to a recipient with a subject and body."""
    msg = EmailMessage()
    msg["From"], msg["To"], msg["Subject"] = os.getenv("SMTP_USER"), to, subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(os.getenv("SMTP_USER"), os.getenv("SMTP_APP_PASSWORD"))
        smtp.send_message(msg)

    return f"Email sent to {to}"
```

- **Docstring and type hints:** the LLM only sees these, so they decide when it calls the tool and what it passes in.
- **`EmailMessage`:** it sets the headers and handles UTF-8, which a raw `f"Subject: ..."` string doesn't (it breaks on Urdu text).
- **Port 465 with `SMTP_SSL`:** the connection is encrypted from the start, so no `starttls()` is needed.

## 4. Add it to the agent

```python
agent = create_agent(llm, tools=[send_email])
```

Nothing else changes in your agent code. Test with your own address first.

## Common error

`SMTPAuthenticationError 535` means you used your normal password, left spaces in the App Password, or 2-Step Verification is off.

