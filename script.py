import smtplib, os, sys
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

SMTPserver = 'smtp.gmail.com'
emailaddr = input("Enter email: ")
# May need application specific password if 2auth is used.
emailpass = input("Enter password: ")



with open('recipients.txt', 'r') as f:
    recipients = [line.strip() for line in f if line.strip()]
print("\nLogging In....")
server = smtplib.SMTP(SMTPserver, 587)
server.ehlo()
server.starttls()
try:
    server.login(emailaddr, emailpass)
except Exception as error:
    print("Login Failed!")
    print(f'Error: \n{error}')
    sys.exit()
print("Success!")

msg = MIMEMultipart()
msg['From'] = emailaddr
msg['Subject'] = 'Automated message'

with open('msg.txt', 'r') as f:
    message = f.read()
msg.attach(MIMEText(message, 'plain'))

filename = 'attachment.jpg'
with open(filename, 'rb') as attachment:
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(p)
text = msg.as_string()
for recipient in recipients:
    msg['To'] = recipient
    try:
        server.sendmail(emailaddr, recipient, text)
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")

server.quit()
