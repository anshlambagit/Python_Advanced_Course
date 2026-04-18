from main import api_call
import pytest 

def test_api_call(mocker):

    mock_get = mocker.patch("main.requests.get")
    mock_get.return_value.json.return_value = {"main": {"key": "value"}}

    result = api_call("https://api.openweathermap.org/data/2.5/weather?q=London&appid=1234567890")
    assert result == {"data": {"main": {"key": "value"}}}
