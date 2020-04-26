import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os

def mail(to, subject, text):
    '''sending email to registered person'''
        
    msg = MIMEMultipart()

    #this password and login are saved and you wont see it,
    #if you want give your own options
    msg['From'] = os.environ.get('USER_GMAIL')
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(os.environ.get('USER_GMAIL'), os.environ.get('PWD_GMAIL'))
    mailServer.sendmail(os.environ.get('USER_GMAIL'), to, msg.as_string())
    mailServer.close()
