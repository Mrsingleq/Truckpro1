import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "mrsingle444425@gmail.com"
receiver_email = "mrsingle444425@gmail.com"
password = "jjkludmsoaynqjtr "

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email"

body = "This is a test email"
message.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls() 
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
