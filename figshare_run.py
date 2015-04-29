__author__ = 'felix.shaw@tgac.ac.uk - 28/04/15'

import figshare_methods as fig
from figshare_authenticate import get_credentials


# setup



#make article
#result = fig.make_article(oauth=get_credentials(), headers=headers, client=client)


#get my articles
# result = fig.get_my_articles(oauth=get_credentials())
# print(result)
result = fig.make_article(oauth=get_credentials())
article_id = result['article_id']
#add file to article
result = fig.add_file_to_article(oauth=get_credentials(), article_id=article_id,
                                 filename='/Users/fshaw/Downloads/COPO-Architecture.pdf')

#delete article
#fig.delete_article(oauth=get_credentials(), article_id=1397475)

print(result)