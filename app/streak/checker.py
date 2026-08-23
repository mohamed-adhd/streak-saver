import smtplib
import os
from email.message import EmailMessage


def alert():
    msg = EmailMessage()
    msg["Subject"] = "yo get some work done, dawg 💀"
    msg["From"] = "streaksaver.adhd@example.com"
    msg["To"] = "midouamdouni4@gmail.com"
    msg.set_content(
        "cmon nigga get tf off valorant and lock in"
    )
    html_body = """\
    <html>
      <body style="background-color:#111; padding:30px; font-family:'Segoe UI', Arial, sans-serif;">
        <div style="max-width:500px; margin:auto; background-color:#1c1c1c; 
                    border-radius:12px; padding:25px; border:2px solid #39ff14;">

          <h1 style="color:#39ff14; font-size:26px; margin-bottom:10px;">
            💀 GET UP DAWG 💀
          </h1>

          <p style="color:#f5f5f5; font-size:17px; line-height:1.5;">
            bro it's getting <b>late as hell</b>, open arch and get some commits going.
          </p>

          <p style="color:#ff5555; font-size:20px; font-weight:bold; margin-top:20px;">
            cmon gang get tf off valorant you aint getting out of silver, lock tf in nigga 🔒
          </p>

          <p style="color:#888; font-size:12px; margin-top:30px;">
            — sent by your antisematic unhinged streak-saving bot
          </p>
        </div>
      </body>
    </html>
    """
    msg.add_alternative(html_body, subtype="html")
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        smtp = os.environ["smtp"]
        server.login("streaksaver.adhd@gmail.com", smtp)
        server.send_message(msg)