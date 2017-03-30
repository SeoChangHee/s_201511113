
# coding: utf-8

# In[3]:

import requests
rResponse=requests.get('http://python.org/')
_html=rResponse.text
print len(_html)


# In[4]:

import urllib
uResponse=urllib.urlopen('http://python.org/')
_html=uResponse.read()
print len(_html)


# In[5]:

from bs4 import BeautifulSoup
tree=BeautifulSoup(_html, "lxml")
strongtags=tree('strong')
for tag in strongtags:
    print tag


# In[6]:

from urllib import urlopen
from bs4 import BeautifulSoup
#_html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
_html = urlopen("http://en.wikipedia.org/wiki/HTML").read()
tree = BeautifulSoup(_html, "lxml")
counter=0
for link in tree.findAll("a"):
    if 'href' in link.attrs:
        if counter<20:
            print counter, link.attrs['href']
        counter+=1
print "Total: ", counter


# In[ ]:




# In[8]:

import lxml.html
from lxml.cssselect import CSSSelector
import requests
re = requests.get('http://www.ieee.org/conferences_events/conferences/search/index.html')

html = lxml.html.fromstring(re.text)
print lxml.html.tostring(html)[:100]


# In[9]:

s=CSSSelector('div.content-r-full table.nogrid-nopad tr p>a[href]')
nodes=s(html)
print len(nodes)


# In[10]:

for node in nodes[:10]:
    print node.text
    print "-----------"
    #print lxml.html.tostring(node)


# In[13]:

get_ipython().run_cell_magic(u'writefile', u'src/ds_web_crawl_ieee.py', u'# coding: utf-8\nimport lxml.html\nfrom lxml.cssselect import CSSSelector\nimport requests\nre = requests.get(\'http://www.ieee.org/conferences_events/conferences/search/index.html\')\n\nhtml = lxml.html.fromstring(re.text)\ns=CSSSelector(\'div.content-r-full table.nogrid-nopad tr p>a[href]\')\nnodes = s(html)\nfor node in nodes:\n    print node.text\n    print "----------"')


# In[14]:

get_ipython().system(u'python src/ds_web_crawl_ieee.py')

