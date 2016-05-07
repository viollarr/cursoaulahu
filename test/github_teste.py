import unittest
from unittest import TestCase, mock
from unittest.mock import Mock
from os import path
import sys

diretorio_desse_arquivo = path.dirname(__file__)
diretorio_huaula = path.join(diretorio_desse_arquivo, '..')
diretorio_huaula = path.abspath(diretorio_huaula)
sys.path.append(diretorio_huaula)

from cursoaulahu import github

GET_MOCK_RESULT = """
{
  "login": "viollarr",
  "id": 2787697,
  "avatar_url": "https://avatars.githubusercontent.com/u/2787697?v=3",
  "gravatar_id": "",
  "url": "https://api.github.com/users/viollarr",
  "html_url": "https://github.com/viollarr",
  "followers_url": "https://api.github.com/users/viollarr/followers",
  "following_url": "https://api.github.com/users/viollarr/following{/other_user}",
  "gists_url": "https://api.github.com/users/viollarr/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/viollarr/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/viollarr/subscriptions",
  "organizations_url": "https://api.github.com/users/viollarr/orgs",
  "repos_url": "https://api.github.com/users/viollarr/repos",
  "events_url": "https://api.github.com/users/viollarr/events{/privacy}",
  "received_events_url": "https://api.github.com/users/viollarr/received_events",
  "type": "User",
  "site_admin": false,
  "name": "Victor Narcizo",
  "company": null,
  "blog": null,
  "location": null,
  "email": "viollarr@gmail.com",
  "hireable": null,
  "bio": null,
  "public_repos": 12,
  "public_gists": 0,
  "followers": 1,
  "following": 0,
  "created_at": "2012-11-13T14:43:21Z",
  "updated_at": "2016-03-10T19:33:45Z"
}"""


class AvatarTests(TestCase):
    @mock.patch('cursoaulahu.github.requests.get')
    @mock.patch('cursoaulahu.github.requests.post')
    def test_avatar_url(self, post_mock, get_mock):
        # teste unitário não pode depender de rede ou da lib request
        response = Mock()
        response.text = GET_MOCK_RESULT
        get_mock.return_value = response
        self.assertEqual('https://avatars.githubusercontent.com/u/2787697?v=3', github.buscar_avatar('viollarr'))
        get_mock.assert_called_once_with('https://api.github.com/users/viollarr')


class IntegracaoTests(TestCase):
    def test_avatar_url(self):
        self.assertEqual('https://avatars.githubusercontent.com/u/3457115?v=3', github.buscar_avatar('renzon'))


if __name__ == '__main__':
    unittest.main()
