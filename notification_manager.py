import os
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.user = os.environ['USER']
        self.password = os.environ['PASSWORD']

    def send_sms(self, msg):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
                        .create(
                            body = msg,
                            from_ = "+18329811002",
                            to = "+529981613497"
                        )
        print(message.sid)
