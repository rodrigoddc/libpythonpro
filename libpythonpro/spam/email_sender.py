class Sender:

    def send(self, receiver, sender, subject, description):
        if '@' not in receiver:
            raise EmailInvalid(f'Receiver email invalid: {receiver}')
        return receiver


class EmailInvalid(Exception):
    pass
