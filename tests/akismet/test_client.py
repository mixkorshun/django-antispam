from copy import copy
from unittest import TestCase
from unittest.mock import Mock

from antispam.akismet import client
from antispam.akismet.entities import Request, Comment


class ClientTests(TestCase):
    def setUp(self):
        self.get_connection_backup = client.get_connection
        self.settings_backup = copy(client.settings)

        self.connection = Mock()
        client.get_connection = Mock(return_value=self.connection)
        client.settings = {
            'AKISMET_API_KEY': 'api-key'
        }

    def test_get_connection(self):
        client.get_connection = self.get_connection_backup
        client.settings = self.settings_backup

    def test_submit(self):
        client.submit(Request(), comment=Comment('my comment'), is_spam=True)

        self.assertTrue(self.connection.submit.called)

    def test_check(self):
        client.check(Request(), comment=Comment('my comment'))

        self.assertTrue(self.connection.check.called)
