def js_with_image(plot_div_id):
    return f"""
    var jsNode = document.getElementById('{plot_div_id}');
        var img = document.getElementById("{plot_div_id}").parentElement.getElementsByTagName('img')[0];
        if(img && img.tagName == 'IMG') document.getElementById("{plot_div_id}").parentElement.removeChild(img);
    """
