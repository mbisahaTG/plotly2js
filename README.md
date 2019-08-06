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
pip install git+https://github.com/stoolan/plotly2js.git
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
