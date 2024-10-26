# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#differences-between-parsers
# BeautifulSoup is used to parse the html or xml data
# html - hyper text markup language - static data to dispaly in web page or web application (html5lib)
# xml - extensive markup language - used to exchange the data between applications (lxml)
from bs4 import BeautifulSoup


html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link1">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup(markup=html_doc, features="html.parser")

# soup.prettify() - Pretty-print this PageElement as a string.
# soup.title - to get the title
# soup.tile.name - prints the tag name
# soup.title.string or soup.title.text - prints the tag string
# soup.title.parent - navigating to parent tag
# soup.find_all(tag) - to get the list of tags - soup.find_all('a') or soup.find_all(id='link1')
# soup.find(tag) or soup.find(tag, class_='value') - to get the first available tag item
# soup.get_text() - to get the text from html or xml
# soup.find(tag).__dict__ - stores the available info of the tag

# print(soup.find(id='link1').__dict__)

"""
{'parser_class': <class 'bs4.BeautifulSoup'>, 'name': 'a', 'namespace': None, '_namespaces': {}, 'prefix': None, 
'sourceline': 6, 'sourcepos': 0, 'known_xml': False, 'attrs': {'href': 'http://example.com/elsie', 'class': ['sister'], 
'id': 'link1'}, 'contents': ['Elsie'], 'parent': <p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link1">Tillie</a>;
and they lived at the bottom of a well.</p>, 'previous_element': 'Once upon a time there were three little sisters; and their names were\n', 
'next_element': 'Elsie', 'next_sibling': ',\n', 'previous_sibling': 'Once upon a time there were three little sisters; and their names were\n', 
'hidden': False, 'can_be_empty_element': False, 'cdata_list_attributes': {'*': ['class', 'accesskey', 'dropzone'], 
'a': ['rel', 'rev'], 'link': ['rel', 'rev'], 'td': ['headers'], 'th': ['headers'], 'form': ['accept-charset'], 
'object': ['archive'], 'area': ['rel'], 'icon': ['sizes'], 'iframe': ['sandbox'], 'output': ['for']}, 
'preserve_whitespace_tags': {'textarea', 'pre'}, 'interesting_string_types': (<class 'bs4.element.NavigableString'>, 
<class 'bs4.element.CData'>)}
"""

# soup.find(id='link1').attrs - {'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}
story = soup.find('p', class_='story')
print(story)

matches = story.find_all('a', class_='sister S')
for match in matches:
    print(match.text)
