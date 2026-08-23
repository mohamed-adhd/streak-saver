import smtplib
import os
from email.message import EmailMessage

def alert():
    msg = EmailMessage()
    msg["Subject"] = "My Nigga get some work done !"
    msg["From"] = "streaksaver.adhd@example.com"
    msg["To"] = "midouamdouni4@gmail.com"
    msg.set_content("dawg its getting late , open arch n get some commits going ,cmon gang get off valorant")
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        smtp = os.environ["smtp"]
        server.login("streaksaver.adhd@gmail.com", smtp)
        server.send_message(msg)