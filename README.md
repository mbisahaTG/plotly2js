# plotly2js

Convert Python Plotly objects to valid JavaScript files

# Dependencies
These will be auto-installed when you install with pip
```
plotly==4.0.0
pandas
jsbeautifier
BeautifulSoup
```

# Installation

Install using pip:

```
pip install git+https://github.com/mbisahaTG/plotly2js.git
```

# Usage

```python
from plotly2js import fig2js

print(fig2js.__doc__)
"""
Convert a Plotly figure to a JavScript string representation. Optionally writes to file.
Parameters
----------
fig:
    Figure object or dict representing a figure
plot_div_id: str
    The div id you would like to attach your plotly plot to
file: str or None (default None)
    The file name and path for the newly-created JavaScript file
config: dict or None (default plotly2js.plotly2js.DEFAULT_CONFIG)
    Plotly.js figure config options
before_scripts: list of functions
    List of functions that accept a plot div id and return valid Javascript.
    Theses functions will be called, and their results inserted into the script BEFORE the Plotly Script
    Example usage:
        before_scripts = [
            lambda div_id: f"console.log('I am plotting to {div_id}!')",
            lambda div_id: f"console.log('This message should appear BEFORE Plotly.plot is called.')"
        ]
after_scripts: list of functions
    List of functions that accept a plot div id and return valid Javascript.
    Theses functions will be called, and their results inserted into the script AFTER the Plotly Script
    Example usage:
        after_scripts = [
            lambda div_id: f"console.log('I am plotting to {div_id}!')",
            lambda div_id: f"console.log('This message should appear AFTER Plotly.plot is called.')"
        ]
VALID KEYWORD ARGUMENTS
    See kwargs for `to_html` at https://github.com/plotly/plotly.py/blob/master/packages/python/plotly/plotly/io/_html.py

Returns
-------
str
    Representation of figure as an HTML div string, optionally creating a file.
"""

# Using an example figure
import plotly.express as px
#create example figure
gapminder = px.data.gapminder()
fig = px.scatter_geo(
    gapminder,
    locations="iso_alpha",
    color="continent",
    hover_name="country",
    size="pop",
    animation_frame="year",
    projection="natural earth",
)
# write example figure to test.js
# html body would be <div id="a_div_id"></div>
fig2js(fig, "a_div_id", file="test.js")
```

# Script Injection

`fig2js` provides two entry points for script injection. The optional parameters `before_scripts` and `after_scripts` allow you to inject arbitrary JS code either before or after the extracted Plotly script. These parameters are lists of functions, that, when supplied the `plot_div_id`, return valid JavaScript code. A simple example is given below:

```python

def log_div_id(plot_div_id):
  return "console.log('The div id is: " + plot_div_id + "');"

def log_browser_type(plot_div_id):
  return "console.log(window.navigator.userAgent)"

fig2js(fig, "a_div_id", file="test.js", before_scripts = [log_div_id], after_scripts = [log_browser_type])

```

## Predefined scripts

A list of predefined scripts we might find handy are found in the `scripts` module.
Specifically I've provided a script for removing parent image elements. More scripts can be added as needed.

```python

from plotly2js.scripts import js_with_image

# make figure
fig2js(fig, "a_div_id", file="test.js", before_scripts = [js_with_image])

```
