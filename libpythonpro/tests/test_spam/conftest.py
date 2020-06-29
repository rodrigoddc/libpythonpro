import pytest

from libpythonpro.spam.db import Conection


@pytest.fixture(scope='module')
def conection():
    conection_obj = Conection()
    yield conection_obj
    conection_obj.close()


@pytest.fixture
def session(conection):
    session_obj = conection.generate_session()
    yield session_obj
    session_obj.roll_back()
    session_obj.close()
