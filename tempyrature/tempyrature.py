__all__ = [
    'Converter'
]


class Converter:
    """
    A simple temperature converter.
    """

    def __init__(self) -> None:
        pass


    def celsius2fahrenheit(celsius: float) -> float:
        """
        Converts celsius to fahrenheit.

        Parameters
        ----------
        celsius : float
            The celsius temperature to convert.

        Returns
        -------
        float
            The converted temperature.

        Examples
        --------
        >>> celsius2fahrenheit(25.0)
        77.0
        >>> celsius2fahrenheit(25.3)
        77.53999999999999

        Formula
        -------
        fahrenheit = 1.8 * celsius + 32
        """

        fahrenheit = 1.8 * celsius + 32
        return fahrenheit


    def fahrenheit2celsius(fahrenheit: float) -> float:
        """
        Converts fahrenheit to celsius.

        Parameters
        ----------
        fahrenheit : float
            The fahrenheit temperature to convert.

        Returns
        -------
        float
            The converted temperature.

        Examples
        --------
        >>> fahrenheit2celsius(77.0)
        25.0
        >>> fahrenheit2celsius(25.3)
        25.299999999999994
        
        Formula
        -------
        celsius = (fahrenheit - 32) / 1.8
        """

        celsius = (fahrenheit - 32) / 1.8
        return celsius


    def celsius2kelvin(celsius: float) -> float:
        """
        Converts celsius to kelvin.

        Parameters
        ----------
        celsius : float
            The celsius temperature to convert.

        Returns
        -------
        float
            The converted temperature.

        Examples
        --------
        >>> celsius2kelvin(10.0)
        283.15
        >>> celsius2kelvin(10.7)
        283.84999999999997

        Formula
        -------
        kelvin = celsius + 273.15
        """

        kelvin = celsius + 273.15
        return kelvin


    def kelvin2celsius(kelvin: float) -> float:
        """
        Converts kelvin to celsius.

        Parameters
        ----------
        kelvin : float
            The kelvin temperature to convert.

        Returns
        -------
        float
            The converted temperature.

        Examples
        --------
        >>> kelvin2celsius(283.0)
        9.850000000000023
        >>> kelvin2celsius(283.84)
        10.689999999999998
        
        Formula
        -------
        celsius = kelvin - 273.15
        """

        celsius = kelvin - 273.15
        return celsius


    def fahrenheit2kelvin(fahrenheit: float) -> float:
        """
        Converts fahrenheit to kelvin.

        Parameters
        ----------
        fahrenheit : float
            The fahrenheit temperature to convert.

        Returns
        -------
        float
            The converted temperature.

        Examples
        --------
        >>> fahrenheit2kelvin(80.0)
        299.81666666666666
        >>> fahrenheit2kelvin(25.7)
        300.2055555555555
        
        Formula
        -------
        kelvin = 273.15 + ((fahrenheit - 32.0) * (5.0/9.0))
        """

        kelvin = 273.15 + ((fahrenheit - 32.0) * (5.0/9.0))
        return kelvin


    def kelvin2fahrenheit(kelvin: float) -> float:
        """
        Converts kelvin to fahrenheit.

        Parameters
        ----------
        kelvin : float
            The kelvin temperature to convert.

        Returns
        -------
        float
            The converted temperature.

        Examples
        --------
        >>> kelvin2fahrenheit(299.81666666666666)
        80.00000000000003
        >>> kelvin2fahrenheit(300.2055555555555)
        80.69999999999997
        
        Formula
        -------
        fahrenheit = (kelvin - 273.15) * 9/5 + 32 
        """

        fahrenheit = (kelvin - 273.15) * 9.0/5.0 + 32
        return fahrenheit
