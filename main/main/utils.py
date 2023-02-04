from . import constants


def get_response(url: str, headers: dict = constants.DEFAULT_HEADERS):
    try:
        import requests as r
    except ImportError:
        raise "Not search a requests module."

    response = r.get(url=url, headers=headers)

    if response.status_code != 200:
        raise "Not response content..."

    return response

def get_html_tags(html: str, pattern: str = r'<([a-z]+)+( [a-z\-]+=[a-z0-9\.\'\"\@\#\$\%\^\&\*\/\:]+)*>'):
    import re

    pattern = re.compile(pattern)
    tags = re.findall(pattern, html)

    return tags

def convert_to_tuple(v1: str, v2: str):
    v1: list = [val for val in v1.split(".") if val]
    v2: list = [val for val in v2.split(".") if val]

    v1 = list(map(int, v1))
    v2 = list(map(int, v2))

    return v1, v2