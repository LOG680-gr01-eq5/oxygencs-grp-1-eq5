import unittest
from unittest.mock import patch, MagicMock
from src.main import App


class TestApp(unittest.TestCase):
    @patch('src.main.psycopg2.connect')
    def setUp(self, mock_db):
        self.mock_db_connection = MagicMock()
        mock_db.return_value = self.mock_db_connection

        self.app = App()

    def tearDown(self):
        self.app = None

    @patch('src.main.App.send_action_to_hvac')
    def test_take_action(self, mock_send_action_to_hvac):
        self.app.T_MAX = 25
        self.app.T_MIN = 15

        # Test with temperature above T_MAX
        action = self.app.take_action(26)
        self.assertEqual(action, 'TurnOnAc')
        mock_send_action_to_hvac.assert_called_with('TurnOnAc')

        mock_send_action_to_hvac.reset_mock()

        # Test with temperature below T_MIN
        action = self.app.take_action(14)
        self.assertEqual(action, 'TurnOnHeater')
        mock_send_action_to_hvac.assert_called_with('TurnOnHeater')

    @patch('src.main.psycopg2.connect')
    def test_save_event_to_database(self, mock_db):
        cursor_mock = MagicMock()
        self.mock_db_connection.cursor.return_value = cursor_mock

        timestamp = "2021-01-01 12:00:00"
        temperature = 22.5
        action = "TurnOnAc"

        self.app.save_event_to_database(timestamp, temperature, action)
        cursor_mock.execute.assert_called_once()
        self.mock_db_connection.commit.assert_called_once()


if __name__ == '__main__':
    unittest.main()