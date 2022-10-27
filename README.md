<div align="center"> 

![PyPI](https://img.shields.io/pypi/v/tempyrature?style=for-the-badge)

![PyPI - Downloads](https://img.shields.io/pypi/dm/tempyrature?style=for-the-badge)

![GitHub commit activity](https://img.shields.io/github/commit-activity/w/Lobooooooo14/tempyrature?style=for-the-badge)

![GitHub](https://img.shields.io/github/license/Lobooooooo14/tempyrature?style=for-the-badge)
<div>

# Tempyrature

Tempyrature is a simple Python module to convert temperature scales easily.

***

## Scales

Tempyrature currently supports 3 temperature ranges:

- Celcius
- Fahrenheit
- Kelvin

## Installation

You can install tempyrature in two main ways:

1. [***Pypi***](https://pypi.org/project/tempyrature/):

    Through the command:
    ```
    pip install tempyrature
    ```
    > This command may vary depending on your device.

2. Cloning this repository:

    If you have GIT installed, you can:

    ```
    git clone https://github.com/Lobooooooo14/tempyrature.git
    ```
    This will download this repository to your device, enter the downloaded folder (make sure it is in the same directory as the `setup.py` file) and use the command:
    ```
    pip install .
    ```

## How to use

After you have done the installation, you can use the tempyrature as follows:

```python
from tempyrature import Converter


print(Converter.celsius2fahrenheit(30.5)) #30.5°C
#>>> 86.0
```

## Documentation

You can see the full documentation [***here***](https://github.com/Lobooooooo14/tempyrature/wiki/Documentation)
