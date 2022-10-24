import tempyrature


def test_float_celsius2fahrenheit():
    assert type(tempyrature.Converter.celsius2fahrenheit(10.3)) == float


def test_correct_response_celsius2fahrenheit():
    assert tempyrature.Converter.celsius2fahrenheit(10.3) == 50.540000000000006


def test_float_celsius2kelvin():
    assert type(tempyrature.Converter.celsius2kelvin(10.3)) == float


def test_correct_response_celsius2kelvin():
    assert tempyrature.Converter.celsius2kelvin(10.3) == 283.45


def test_float_fahrenheit2celsius():
    assert type(tempyrature.Converter.fahrenheit2celsius(34.3)) == float


def test_correct_response_fahrenheit2celsius():
    assert tempyrature.Converter.fahrenheit2celsius(34.3) == 1.2777777777777761


def test_float_fahrenheit2kelvin():
    assert type(tempyrature.Converter.fahrenheit2kelvin(34.3)) == float


def test_correct_response_fahrenheit2kelvin():
    assert tempyrature.Converter.fahrenheit2kelvin(34.3) == 274.42777777777775


def test_float_kelvin2celsius():
    assert type(tempyrature.Converter.kelvin2celsius(280.2)) == float


def test_correct_response_kelvin2celsius():
    assert tempyrature.Converter.kelvin2celsius(280.2) == 7.050000000000011


def test_float_kelvin2fahrenheit():
    assert type(tempyrature.Converter.kelvin2fahrenheit(280.2)) == float


def test_correct_response_kelvin2fahrenheit():
    assert tempyrature.Converter.kelvin2fahrenheit(280.2) == -19.30999999999998
