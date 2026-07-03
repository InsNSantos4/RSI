from smtplib import SMTP
from email.mime.text import MIMEText


class Admin:
    def __init__(self, name: str, email: str, permission_level: int, password: str, smtp_server: str):
        self.name = name
        self.email = email
        self.permission_level = permission_level
        self.password = password
        self.smtp_server = smtp_server

    def send_email(self, host_ip):
            smtp_server_name = self.smtp_server
            smtp_port = 587
            username = self.email
            password = self.password

            sender_email = self.email
            
            receiver_email = self.email
            subject = "Alert"
            body = f"Hello {self.name}, your machine with ip {host_ip} has gone down."

            message = MIMEText(body, "plain")
            message["Subject"] = subject
            message["From"] = sender_email
            message["To"] = receiver_email

            with SMTP(smtp_server_name, smtp_port) as server:
                 server.starttls()
                 server.login(username, password)
                 server.sendmail(sender_email, receiver_email, message.as_string())