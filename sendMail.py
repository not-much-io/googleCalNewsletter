import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config
class mailer:
    body =""

    def __init__(self, subject, body):
        self.subject = subject
        self.body = body

    def SendMail(self):
        fromaddr = config.conf['fromEmail']
        toaddr  = config.conf['toEmail']
        password = config.conf['password']

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Olen Kirja pealkiri"

        body = self.body
        # plain may be more practical. But with html we could use more fancier template for newsletter.
        msg.attach(MIMEText(body, 'plain'))
        #msg.attach(MIMEText(body, 'html'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

