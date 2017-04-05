
# coding: utf-8

# In[7]:



import lxml.html 
import requests 

 
keyword='윤딴딴' 
response = requests.get("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0") 
_html = lxml.html.fromstring(response.text) 

 
from lxml.cssselect import CSSSelector 

 
selector = CSSSelector('table[summary] > tbody > ._tracklist_move')    
nodes = selector(_html) 

 
_selName = CSSSelector('.name > a.title') 
_selArtist = CSSSelector('._artist.artist') 
_selAlbum= CSSSelector('.album > a') 

for node in nodes: 
#print lxml.html.tostring(item) 
    _name=_selName(node) 
    _artist=_selArtist(node) 
    _album=_selAlbum(node) 
    if _name: 
        print _artist[0].text_content().strip(), 
        print "---", 
        print _name[0].text_content(), 
        print "---",         
        print _album[0].text_content() 

