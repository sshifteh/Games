import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'
r = requests.get(url)
r_html = r.text # the html of the page as a string is not in this variable lol


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.prettify())
print soup.title          # <title>The Dormouse's story</title>
print soup.title.name     # titl
print soup.title.string   #The Dormouse's story


#print soup.find_all('a')
#print soup.find(id="link3")
#print soup.find(title)

#soup = BeautifulSoup(html_doc, "html.parser" )

for t in soup.find_all('title'):
    print t.title.string


