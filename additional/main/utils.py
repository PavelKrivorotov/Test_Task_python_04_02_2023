import requests as r

from . import constants


def get_response(
        url: str = constants.DEFAULT_URL,
        query: str = constants.DEFAULT_QUERY_PARAMS
    ) -> dict:
    
    response = r.post(url=url, json={"query":query})

    if response.status_code != 200:
        raise ValueError("Not correct request.")

    json = response.json()
    return json