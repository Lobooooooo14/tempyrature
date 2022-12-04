import tempyrature


def test_float_celsius2fahrenheit():
    assert type(tempyrature.Converter.celsius2fahrenheit(10.3)) == float


def test_float_celsius2kelvin():
    assert type(tempyrature.Converter.celsius2kelvin(10.3)) == float


def test_float_fahrenheit2celsius():
    assert type(tempyrature.Converter.fahrenheit2celsius(34.3)) == float


def test_float_fahrenheit2kelvin():
    assert type(tempyrature.Converter.fahrenheit2kelvin(34.3)) == float


def test_float_kelvin2celsius():
    assert type(tempyrature.Converter.kelvin2celsius(280.2)) == float


def test_float_kelvin2fahrenheit():
    assert type(tempyrature.Converter.kelvin2fahrenheit(280.2)) == float


def test_float_rankine2celsius():
    assert type(tempyrature.Converter.rankine2celsius(10.0)) == float


def test_float_celsius2rankine():
    assert type(tempyrature.Converter.celsius2rankine(10.0)) == float


def test_float_rankine2fahrenheit():
    assert type(tempyrature.Converter.rankine2fahrenheit(10.0)) == float


def test_float_fahrenheit2rankine():
    assert type(tempyrature.Converter.fahrenheit2rankine(104.0)) == float


def test_float_rankine2kelvin():
    assert type(tempyrature.Converter.rankine2fahrenheit(563.6700000000001)) == float


def test_float_kelvin2rankine():
    assert type(tempyrature.Converter.kelvin2rankine(313.15000000000003)) == float

