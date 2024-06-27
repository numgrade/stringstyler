"""Init file for colortext package.

This file is used to define the package's public API.

The public API consists of the following functions:
- print_color_text: A function to print colored text to the console.
- color_text: A decorator to return colored text.

The __version__ variable is also defined in this file.
"""

import importlib.metadata
from .colortext import print_color_text, color_text


# get version from pyproject.toml / colortext is the package name
__version__ = importlib.metadata.version("colortext")