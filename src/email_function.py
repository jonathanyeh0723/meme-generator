"""Import libraries for this email module."""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class Email:
    """
    Define Email class.

    It needs 2 positional argument to instantiate a class.
    And a method to send email with .png image attachment.
    """

    def __init__(self, sender_address, sender_passwd):
        """Class init."""
        self.sender_address = sender_address
        self.sender_passwd = sender_passwd

    def send(self, receiver_address, subject, content, attach_file_name):
        """
        Send email with attached image.

        Arguments:
            receiver_address {str} -- the receiver's email address.
            subject {str} -- head of the mail.
            content {str} -- body of the email.
            attach_file_name {str} -- attached image name.
        Returns:
            a string with recipient mail address.
        
        """
        message = MIMEMultipart()
        message['From'] = self.sender_address
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
        session.login(self.sender_address, self.sender_passwd)
        text = message.as_string()
        session.sendmail(self.sender_address, receiver_address, text)
        session.quit()

        return f'Send email to {receiver_address}.'
