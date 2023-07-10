import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

user_name = "dextereltester@gmail.com"
password = "wanfuhgdptbshodu"

receiver = "dextereltester@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: AUTOMATIC EMAIL TEST
Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(user_name, password)
    server.sendmail(user_name, receiver, message)
