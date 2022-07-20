import smtplib

sender = "lucian1611@gmail.com"
receiver = "lucian1611@yahoo.com"
password = "Lucian1984$"
subject = "Python email test"
body = "Te salut!"

#header
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    print("logged in...")
    server.sendmail(sender, receiver, message)
    print("email-ul s-a trimis")
except smtplib.SMTPAuthenticationError:
    print("unable to sign in")