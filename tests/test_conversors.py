import tempyrature


def test_correct_response_celsius2fahrenheit():
    assert tempyrature.Converter.celsius2fahrenheit(10.3) == 50.540000000000006


def test_correct_response_celsius2kelvin():
    assert tempyrature.Converter.celsius2kelvin(10.3) == 283.45


def test_correct_response_fahrenheit2celsius():
    assert tempyrature.Converter.fahrenheit2celsius(34.3) == 1.2777777777777761


def test_correct_response_fahrenheit2kelvin():
    assert tempyrature.Converter.fahrenheit2kelvin(34.3) == 274.42777777777775


def test_correct_response_kelvin2celsius():
    assert tempyrature.Converter.kelvin2celsius(280.2) == 7.050000000000011


def test_correct_response_kelvin2fahrenheit():
    assert tempyrature.Converter.kelvin2fahrenheit(280.2) == 44.69000000000002


def test_correct_response_rankine2celsius():
    assert tempyrature.Converter.rankine2celsius(509.66999999999996) == 10.0


def test_correct_response_celsius2rankine():
    assert tempyrature.Converter.celsius2rankine(10.0) == 509.66999999999996


def test_correct_response_rankine2fahrenheit():
    assert tempyrature.Converter.rankine2fahrenheit(563.6700000000001) == 104.00000000000006


def test_correct_response_fahrenheit2rankine():
    assert tempyrature.Converter.fahrenheit2rankine(104.0) == 563.6700000000001


def test_correct_response_rankine2kelvin():
    assert tempyrature.Converter.rankine2kelvin(563.6700000000001) == 313.15000000000003


def test_correct_response_kelvin2rankine():
    assert tempyrature.Converter.kelvin2rankine(313.15000000000003) == 563.6700000000001