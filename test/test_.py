import pytest
from unittest.mock import patch, MagicMock
from src.main import App


@pytest.fixture
def app():
    with patch('src.main.psycopg2.connect') as mock_db:
        mock_db_connection = MagicMock()
        mock_db.return_value = mock_db_connection
        app_instance = App()
        app_instance.mock_db_connection = mock_db_connection
        yield app_instance


def test_take_action(app):
    with patch('src.main.App.send_action_to_hvac') as mock_send_action_to_hvac:
        app.T_MAX = 25
        app.T_MIN = 15

        # Test with temperature above T_MAX
        action = app.take_action(26)
        assert action == 'TurnOnAc'
        mock_send_action_to_hvac.assert_called_with('TurnOnAc')

        mock_send_action_to_hvac.reset_mock()

        # Test with temperature below T_MIN
        action = app.take_action(14)
        assert action == 'TurnOnHeater'
        mock_send_action_to_hvac.assert_called_with('TurnOnHeater')


def test_save_event_to_database(app):
    cursor_mock = MagicMock()
    app.mock_db_connection.cursor.return_value = cursor_mock

    timestamp = "2021-01-01 12:00:00"
    temperature = 22.5
    action = "TurnOnAc"

    app.save_event_to_database(timestamp, temperature, action)
    cursor_mock.execute.assert_called_once()
    app.mock_db_connection.commit.assert_called_once()