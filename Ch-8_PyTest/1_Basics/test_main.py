from main import weather_check

# Test cases for weather_check function
def test_weather_check():
    assert weather_check(-5) == "It's freezing outside!"
    assert weather_check(10) == "It's a bit chilly."
    assert weather_check(20) == "The weather is pleasant."
    assert weather_check(30) == "It's hot outside!"


if __name__ == "__main__":
    test_weather_check()
    