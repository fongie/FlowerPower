import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class NotificationSender:
    '''
    Responsible for sending notifications to a user email concerning moistness values and waterings.
    '''

    #note: smtplib cannot send swedish chars?
    def __init__(self, plantID, sendToEmail):
        '''
        Constructor. Parameters: plantID (int), current plants ID
                                sendToEmail (str), email to send notification to
        '''
        self.username = "flowerpowerkth@gmail.com"
        self.password = ""
        self.plantID = plantID
        self.to_addr = sendToEmail

    def sendDrynessNotification(self, moistnessValue):
        '''
        Sends a notification warning about a moistness value
        '''
        subj = "Your plant number {} is running low on water!".format(self.plantID)
        body = "Hi! Plant nr {} now has a moistness value of {}, which is lower than recomended. Time to water the plant!".format(self.plantID, moistnessValue)
        self._send_email(subj,body)
        return True

    def sendWateringNotification(self):
        '''
        Sends notification that the plant is being watered
        '''
        subj = "Your plant number {} is being watered!".format(self.plantID)
        body = "Hi! Plant nr {} is now being watered automatically due to low moistness values.".format(self.plantID)
        self._send_email(subj,body)
        return True

    def setEmail(self,email):
        '''
        Set a new email to send notifications to
        '''
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
