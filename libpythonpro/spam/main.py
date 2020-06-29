class SpamSender:

    def __init__(self, session, sender):
        self.session = session
        self.sender = sender

    def send_email(self, sender, subject, description):
        for user in self.session.list():
            self.sender.send(
                sender,
                user.email,
                subject,
                description
            )
