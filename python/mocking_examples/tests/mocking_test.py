from unittest.mock import patch

from src import mocking_examples 

def test_older_times_two():
    result = mocking_examples.older_times_two(5)
    assert result == 10


@patch('src.mocking_examples.older_times_two')
def test_with_a_mock_person_older(
    mock_older_times_two
):
    # this patch value here is on the return of the expected function
    # which shows that 99999 overwrites the supplied 31 * 2 = 62 to
    # older_times_two when the function runs
    mock_older_times_two.return_value = 99999

    # actually call the logic you want
    result = mocking_examples.person_older("Nate", 31)

    # assert function(s) were called even when patched
    # this must be called after you run the function(s)
    mock_older_times_two.assert_called_once_with(31)

    assert result == "Nate is 99999"