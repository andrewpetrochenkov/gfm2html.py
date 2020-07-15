__all__ = ['gfm2html']

import json

import requests_retry_on_exceptions as requests

URL = 'https://api.github.com/markdown'


def gfm2html(text, token=None):
    headers = {"Authorization": "Bearer %s" % token} if token else {}
    data = json.dumps({"text": text, "mode": "gfm"})
    r = requests.post(URL, data=data, headers=headers)
    r.raise_for_status()
    return r.text
