from plotly.io._html import to_html
import re, jsbeautifier
from bs4 import BeautifulSoup

def set_config(filename):
    DEFAULT_CONFIG = {
        "modeBarButtonsToRemove": [
            "sendDataToCloud",
            "autoScale2d",
            "hoverClosestCartesian",
            "hoverCompareCartesian",
            "lasso2d",
            "select2d",
            "zoom2d",
            "pan2d",
            "zoomIn2d",
            "zoomOut2d",
            "toggleSpikelines",
        ],
        "displaylogo": False,
        "responsive": True,
        "toImageButtonOptions": {
            'format': 'png',
            'filename': 'Copyright_TeleGeography_' + filename
        }
    }
    return DEFAULT_CONFIG


def write_to_file(js, filename):
    with open(filename, "w") as f:
        f.write(js)


def fig2js(
    fig,
    plot_div_id,
    file=None,
    #config=DEFAULT_CONFIG,
    config=None,
    before_scripts=[],
    after_scripts=[],
    **kwargs
):
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
    DEFAULT_KWARGS = dict(
        auto_play=True,
        include_plotlyjs=False,
        include_mathjax=False,
        post_script=None,
        full_html=False,
        animation_opts=None,
        default_width="100%",
        default_height="100%",
        validate=True,
    )
    DEFAULT_KWARGS.update(kwargs)
    html = to_html(fig, config=set_config(plot_div_id), **DEFAULT_KWARGS)
    soup = BeautifulSoup(html, features="html.parser")
    div_id = soup.find("div", {"class": "plotly-graph-div"})["id"]
    script = soup.find("script").string
    assert div_id in script, "Error, script not found"
    assert "PLOTLYENV" in script
    script = script.replace(div_id, plot_div_id)
    for custom_script in before_scripts:
        script = custom_script(plot_div_id) + "\n" + script
    for custom_script in after_scripts:
        script = script + "\n" + custom_script(plot_div_id)
    script = (
        "document.addEventListener('DOMContentLoaded', function(event) {"
        + script
        + "});"
    )
    script = jsbeautifier.beautify(script)
    if file is not None:
        write_to_file(script, file)
    return script


def test():
    import plotly.express as px

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
    fig2js(fig, "a_div_id", file="test.js")


if __name__ == "__main__":
    test()
