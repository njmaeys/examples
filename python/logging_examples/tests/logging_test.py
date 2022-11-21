from unittest.mock import patch

from src import logging_examples

@patch('logging.Logger.warning')
def test_simple_log(
    mock_log
):
    logging_examples.simple_log()

    mock_log.assert_called_once_with('Warning message')
