from libpythonpro.spam.models import User


def test_user_save(session):
    user = User(name='Rodrigo', email='rodrigo@mail.com')
    session.save(user)
    assert isinstance(user.id, int)


def test_user_list(conection, session):
    users = [
        User(name='Rodrigo', email='rodrigo@mail.com'),
        User(name='Mestre', email='rodrigo@mail.com')
    ]

    for user in users:
        session.save(user)

    assert users == session.list()
    session.roll_back()
    session.close()
    conection.close()
