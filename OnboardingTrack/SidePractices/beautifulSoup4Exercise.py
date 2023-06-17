from bs4 import BeautifulSoup, Tag, SoupStrainer
import requests

# soup = BeautifulSoup('<p class = "boldest"> This is very rediculous </p>', 'lxml')
# attr = soup.p
# attr['class'] = "slimy duck"
# # print(soup)
# # print(attr)


# print(soup.contents[0].name)



# url = "https://www.tutorialspoint.com/index.htm"
# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")
# print(soup.title)


# html = '''<b>tutorialspoint</b>, <i>&web scraping &data science;</i>'''
# soup = BeautifulSoup(html, 'lxml')
# print(soup)

#Comparing objects for equality
markup = "<p>Learn Python and <b>Java</b> and advanced <b>Java</b>! from Tutorialspoint</p>"
soup = BeautifulSoup(markup, "html.parser")
first_b, second_b = soup.find_all('b')
# print(first_b, second_b)
# print(first_b == second_b)
# print(first_b is second_b)
      
#Copying Beautiful Soup objects)
import copy
p_copy = copy.copy(soup)
print(p_copy == soup)
print(soup is p_copy)

#SoupStrainer
def is_short(str):
    return len(str) < 10

rest = SoupStrainer(str = is_short)
