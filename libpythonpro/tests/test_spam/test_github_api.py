from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    answer_mock = Mock()
    url = 'https://avatars0.githubusercontent.com/u/17282736?v=4'
    answer_mock.json.return_value = {
        'login': 'rodrigoddc',
        'id': 17282736,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = answer_mock
    return url


def test_search_avatar(avatar_url):
    url = github_api.search_avatar('rodrigoddc')
    assert url == avatar_url


def test_search_avatar_integration():
    url = github_api.search_avatar('rodrigoddc')
    assert url == 'https://avatars0.githubusercontent.com/u/17282736?v=4'
