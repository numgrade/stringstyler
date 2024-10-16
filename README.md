
# stringstyler

**Add color and change the format of your strings !**

[![PyPI Version](https://img.shields.io/pypi/pyversions/stringstyler)](https://pypi.org/project/stringstyler/)
[![License](https://img.shields.io/badge/license-new%20BSD-blue.svg)](https://github.com/numgrade/stringstyler/blob/main/LICENSE)
![Python 3](https://img.shields.io/badge/python-3-blue.svg)

---

## Installation

Create and activate a virtual environment and then install stringstyler:

```console
$ pip install stringstyler

---> 100%
```

## Usage

### The print_color_text() function

```python
from stringstyler import print_styler


print_color_text('Hello, World!', 'red')
print_color_text('Hello, World!', 'red', style='bold')
print_color_text('Hello, World!', 'green', style='underline')
print_color_text('Hello, World!', 'blue', style='reverse')
print_color_text('Hello, World!', 'magenta', style='invisible')
print_color_text('Hello, World!', 'cyan', style='strikethrough')
```

### The text_styler decorator

```python
from stringstyler import text_styler

@text_styler(color="yellow", style="bold")
def greet(name: str):
    """Greets a person by name."""
    return f"Hello, {name}!"
```

## License

This project is licensed under the terms of the MIT license.