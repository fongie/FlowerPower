import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''
Responsible for sending notifications to a user email concerning moistness values and waterings.
'''
class NotificationSender:

    #note: smtplib cannot send ÅÄÖ?
    '''
    Instantiated with the current plantID and which email to send notifications to
    '''
    def __init__(self, plantID, sendToEmail):
        self.username = "flowerpowerkth@gmail.com"
        self.password = ""
        self.plantID = plantID
        self.to_addr = sendToEmail

    '''
    Sends a notification warning about a moistness value
    '''
    def sendDrynessNotification(self, moistnessValue):
        subj = "Your plant number {} is running low on water!".format(self.plantID)
        body = "Hi! Plant nr {} now has a moistness value of {}, which is lower than recomended. Time to water the plant!".format(self.plantID, moistnessValue)
        self._send_email(subj,body)
        return True

    '''
    Sends notification that the plant is being watered
    '''
    def sendWateringNotification(self):
        subj = "Your plant number {} is being watered!".format(self.plantID)
        body = "Hi! Plant nr {} is now being watered automatically due to low moistness values.".format(self.plantID)
        self._send_email(subj,body)
        return True

    def setEmail(self,email):
        self.to_addr = email

    def _send_email(self, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = self.to_addr
        msg['Subject'] = subject
        msg.attach(MIMEText(body, "plain"))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(self.username, self.to_addr, msg.as_string())
        server.quit
