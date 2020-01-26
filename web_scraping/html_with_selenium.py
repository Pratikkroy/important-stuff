from selenium import webdriver
from bs4 import BeautifulSoup

# # install driver
# driver_path = r'/Users/roypra/Documents/phantomjs-2.1.1-macosx/bin/phantomjs'
# # driver = webdriver.Chrome(executable_path= r'/Users/roypra/Documents/chromedriver')
# driver = webdriver.PhantomJS(executable_path = driver_path)

# source_page_url = 'https://www.imdb.com//title/tt0111161/'
# driver.get(source_page_url)

# html_doc = driver.page_source

html_doc = """
<html>
	<head>
		<title>The Dormouse's story</title>
	</head>
<body>
	<p class="title">
		<b>The Dormouse's story</b>
	</p>
	<p class="story">Once upon a time there were three little sisters; and their names were
	<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
	<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
	<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
	and they lived at the bottom of a well.</p>
	<p class="story">...</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'lxml')
# print(soup.prettify())

# search first p tag
first_p_tag = soup.find('p')
# print(first_p_tag.prettify())

a_tags = soup.find_all('a')
# print(len(a_tags))

p_tag = soup.find('p', class_ = 'story')

a = soup.find_all('a', {'id':'link1'})

a_elsie = soup.find_all('a', string = 'Elsie')
# print(a_elsie)

# search for all child
p = soup.find('p', class_ = 'story')
all_p_children = p.findChildren()
# print(all_p_children)

# search for all parent
p = soup.find('p', class_ = 'story')
p_parent = p.findParent()
# print(p_parent)


# search for sibling
first_a = soup.find('a')
remain_sibling = first_a.find_next_sibling()
print(remain_sibling)




# driver.quit()