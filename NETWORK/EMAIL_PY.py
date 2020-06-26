import os
import smtplib

def Email_send():
    EMAIL_USER = os.environ.get("EMAIL_USER")
    EMAIL_PASS = os.environ.get("EMAIL_PASS")

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(EMAIL_USER, EMAIL_PASS)

    msg = 'Subject: "TEST email - plz ignore"\n\n"TEST email - plz ignore"'
    server.sendmail(
        EMAIL_USER,
        EMAIL_USER,
        msg)
    server.quit()




