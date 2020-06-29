from unittest.mock import Mock

import pytest

from libpythonpro.spam.email_sender import Sender
from libpythonpro.spam.main import SpamSender
from libpythonpro.spam.models import User


@pytest.mark.parametrize(
    'users',
    [
        [
            User(name='Rodrigo', email='rodrigo@mail.com'),
            User(name='Mestre', email='rodrigo@mail.com')
        ],
        [
            User(name='Rodrigo', email='rodrigo@mail.com')
        ]
    ]
)
def test_quantity_spam(session, users):
    for user in users:
        session.save(user)

    sender = Mock()
    spam_sender = SpamSender(session, sender)
    spam_sender.send_email(
        'send@a.com',
        'Some Subject',
        'Some description'
    )
    assert len(users) == sender.send.call_count


def test_parameters_spam(session):
    user = User(name='Rodrigo', email='rodrigo@mail.com')
    session.save(user)

    sender = Mock()
    spam_sender = SpamSender(session, sender)
    spam_sender.send_email(
        'some_sender@a.com',
        'Some Subject',
        'Some description'
    )
    sender.send.assert_called_once_with(
        'some_sender@a.com',
        'rodrigo@mail.com',
        'Some Subject',
        'Some description',
    )
