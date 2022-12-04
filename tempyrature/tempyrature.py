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
        
        Formula
        -------
        fahrenheit = (kelvin - 273.15) * 9/5 + 32 
        """

        fahrenheit = (kelvin - 273.15) * 9.0/5.0 + 32
        return fahrenheit


    def celsius2rankine(celsius: float) -> float:
        """
        Converts celsius to rankine.

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
        >>> celsius2rankine(10.0)
        509.66999999999996
        
        Formula
        -------
        rankine = (celsius + 273.15) * 9/5
        """

        rankine = (celsius + 273.15) * 9/5
        return rankine


    def rankine2celsius(rankine: float) -> float:
        """
        Converts rankine to celsius.

        Parameters
        ----------
        rankine : float
            The rankine temperature to convert.

        Returns
        -------
        float
            The converted temperature.

        Examples
        --------
        >>> rankine2celsius(509.66999999999996)
        10.0
        
        Formula
        -------
        celsius = rankine * 5/9 - 273.15
        """

        celsius = rankine * 5/9 - 273.15
        return celsius


    def fahrenheit2rankine(fahrenheit: float) -> float:
        """
        Converts fahrenheit to rankine.

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
        >>> fahrenheit2rankine(104.0)
        563.6700000000001
        
        Formula
        -------
        rankine = fahrenheit + 459.67
        """

        rankine = fahrenheit + 459.67
        return rankine


    def rankine2fahrenheit(rankine: float) -> float:
        """
        Converts rankine to fahrenheit.

        Parameters
        ----------
        rankine : float
            The rankine temperature to convert.

        Returns
        -------
        float
            The converted temperature.

        Examples
        --------
        >>> rankine2fahrenheit(563.6700000000001)
        104.00000000000006
        
        Formula
        -------
        fahrenheit = rankine - 459.67
        """

        fahrenheit = rankine - 459.67
        return fahrenheit


    def kelvin2rankine(kelvin: float) -> float:
        """
        Converts kelvin to rankine.

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
        >>> kelvin2rankine(313.15000000000003)
        563.6700000000001
        
        Formula
        -------
        rankine = kelvin * 9/5
        """

        rankine = kelvin * 9/5
        return rankine


    def rankine2kelvin(rankine: float) -> float:
        """
        Converts rankine to kelvin.

        Parameters
        ----------
        rankine : float
            The rankine temperature to convert.

        Returns
        -------
        float
            The converted temperature.

        Examples
        --------
        >>> rankine2kelvin(563.6700000000001)
        313.15000000000003
        
        Formula
        -------
        kelvin = rankine * 5/9
        """

        kelvin = rankine * 5/9
        return kelvin
