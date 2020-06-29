import pytest

from libpythonpro.spam.email_sender import Sender, EmailInvalid


def test_create_email_sender():
    sender = Sender()
    assert sender is not None


@pytest.mark.parametrize(
    'receiver',
    ['receiver@python.pro.br', 'foo@bar.com.br']
)
def test_receiver(receiver):
    sender = Sender()

    result = sender.send(
        receiver,
        'sender@python.pro.br',
        'Some subject',
        'Some a bit short description'
    )

    assert receiver in result


@pytest.mark.parametrize(
    'receiver',
    ['', 'foo!bar.com.br']
)
def test_sender(receiver):
    sender = Sender()

    with pytest.raises(EmailInvalid):
        sender.send(
            receiver,
            'sender@python.pro.br',
            'Some subject',
            'Some a bit short description'
        )
