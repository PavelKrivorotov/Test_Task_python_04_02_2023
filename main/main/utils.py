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

def convert_to_list(v: str):
    v: list = [val for val in v.split(".") if val]
    v = list(map(int, v))

    try:
        while not v[-1]:
            v.pop()
    except IndexError:
        pass

    return v