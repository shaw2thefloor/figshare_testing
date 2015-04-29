__author__ = 'felix.shaw@tgac.ac.uk - 28/04/15'
import requests

import figshare_methods as fig
from figshare_authenticate import get_credentials


# setup
headers = {'content-type': 'application/json'}
client = requests.session()

#make article
#result = fig.make_article(oauth=get_credentials(), headers=headers, client=client)


#get my articles
result = fig.get_my_articles(oauth=get_credentials(), headers=headers, client=client)

#delete article
#response = client.delete(url + '/1396515', auth=oauth, headers=headers)

print(result)