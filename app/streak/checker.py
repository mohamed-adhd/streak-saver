import os
import smtplib
from email.message import EmailMessage

v1 = """\
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

v2= """\
<html>
  <body style="background-color:#0d0d0d; padding:30px; font-family:'Courier New', monospace;">
    <div style="max-width:500px; margin:auto; background-color:#181818;
                border-radius:8px; padding:25px; border:2px dashed #ff9900;">
      <h1 style="color:#ff9900; font-size:24px; margin-bottom:10px;">
        ⚠️NATENYAHU IS DOING THIS⚠️
      </h1>
      <p style="color:#eee; font-size:16px; line-height:1.6;">
        yo fr fr you really about to let this streak die over a video game designed by isreal??
      </p>
      <p style="color:#ffcc00; font-size:19px; font-weight:bold; margin-top:15px;">
        open arch. commit something. anything. right now.
      </p>
      <p style="color:#666; font-size:12px; margin-top:25px;">
        — the nigga standing on buisness
      </p>
    </div>
  </body>
</html>
"""

v3= """\
<html>
  <body style="background-color:#050510; padding:30px; font-family:'Trebuchet MS', sans-serif;">
    <div style="max-width:500px; margin:auto; background-color:#12121f;
                border-radius:16px; padding:25px; border:2px solid #ff00ff;">
      <h1 style="color:#ff00ff; font-size:28px; margin-bottom:10px; letter-spacing:1px;">
        🚨 LAST TIME I SEND THE MESSAGE🚨
      </h1>
      <p style="color:#e0e0e0; font-size:17px; line-height:1.5;">
        it's late, you're still queued up, and your github is collecting dust ngl.
      </p>
      <p style="color:#00ffff; font-size:21px; font-weight:bold; margin-top:20px;">
        you got 20 min to commit , else i ll do that , since you sa bitch
      </p>
      <p style="color:#777; font-size:12px; margin-top:30px;">
        — ay fuck u nigga , sincerly
      </p>
    </div>
  </body>
</html>
"""





def alert(number):
    msg = EmailMessage()
    msg["Subject"] = "My Nigga get some work done !"
    msg["From"] = "streaksaver.adhd@gmail.com"
    msg["To"] = "midouamdouni4@gmail.com"

    msg.set_content(
        "bro it's getting late as hell, open arch and get some commits going, "
    )
    if (number==1):
        html_body = v1
    elif (number==2):
        html_body = v2
    elif (number==3):
        html_body = v3


    msg.add_alternative(html_body, subtype="html")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        smtp = os.environ["smtp"]
        server.login("streaksaver.adhd@gmail.com", smtp)
        server.send_message(msg)