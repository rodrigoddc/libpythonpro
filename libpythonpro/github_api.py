import requests


def search_avatar(username: str) -> str:
    """
    Search for user avatar link on Github API
    :param username: (str) username on Github
    :return: (str) link to user avatar
    """

    url = f'https://api.github.com/users/{username}'
    answer = requests.get(url)
    return answer.json()['avatar_url']


if __name__ == '__main__':
    print(search_avatar('rodrigoddc'))
