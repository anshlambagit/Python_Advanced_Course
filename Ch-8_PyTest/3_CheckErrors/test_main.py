from main import weather 
import pytest


# Test cases for weather_check method
def test_weather_check():
    w = weather()
    assert w.weather_check(-5) == "It's freezing outside!"
    assert w.weather_check(10) == "It's a bit chilly."
    assert w.weather_check(20) == "The weather is pleasant."
    assert w.weather_check(30) == "It's hot outside!"

# Test cases for rain_check method
def test_rain_check():
    w = weather()
    assert w.rain_check(0.8) == "It's likely to rain. Don't forget your umbrella!"
    assert w.rain_check(0.5) == "There's a chance of rain. You might want to carry an umbrella."
    assert w.rain_check(0.2) == "It's unlikely to rain today."

# Test cases for divide method
def test_divide():
    w = weather()
    assert w.divide(10, 2) == 5
    assert w.divide(9, 3) == 3
    
    with pytest.raises(ValueError,match="Cannot divide by zero!"):
        w.divide(10, 0)