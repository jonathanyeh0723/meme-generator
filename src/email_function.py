import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class Email:

    sender_address = 'memegenerator886@gmail.com'
    sender_passwd = 'BeautifulMeme2021'

    @classmethod
    def send(cls, receiver_address, subject, content, attach_file_name):

        message = MIMEMultipart()
        message['From'] = cls.sender_address
        message['To'] = receiver_address
        message['Subject'] = subject

        message.attach(MIMEText(content, 'plain'))
        attach_file = open(attach_file_name, 'rb')

        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload)

        payload.add_header('Content-Disposition', 'attachment',
                           filename=attach_file_name)
        message.attach(payload)

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(cls.sender_address, cls.sender_passwd)
        text = message.as_string()
        session.sendmail(cls.sender_address, receiver_address, text)
        session.quit()

        return f'Send email to {receiver_address}.'
