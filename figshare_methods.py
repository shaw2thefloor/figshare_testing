__author__ = 'felix.shaw@tgac.ac.uk - 29/04/15'
import json


def make_article(oauth=None, client=None, headers=None):
    url = 'http://api.figshare.com/v1/my_data/articles'
    body = {'title': 'COPO ARTICLE', 'description': 'COPO DESCRIPTION', 'defined_type': 'paper'}
    response = client.post(url, auth=oauth, data=json.dumps(body), headers=headers)
    return json.loads(response.content.decode("utf-8"))


def get_my_articles(oauth=None, client=None, headers=None):
    url = 'http://api.figshare.com/v1/my_data/articles'
    response = client.get(url, auth=oauth, headers=headers)
    return json.loads(response.content.decode("utf-8"))