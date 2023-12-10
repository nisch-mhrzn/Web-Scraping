# If you want to scrape a website:
# 1. Use the API
# 2. HTML Web Scraping using some tool like bs4
# STep 0: setting up the environment
import requests
from bs4 import BeautifulSoup
url ='https://codewithharry.com'

#Step 1: Get the html
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

#step 2: Prase the HTML
soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)

#Step3 : HTML tree traversal
#Commonly used types of object
#1.Tag
#bs4.element.NavigableString
#3 BeautifulSoup
#4 Comment

title = soup.title
# print(type(title))

# Get all the paragraphs from the page
paras =  soup.find_all('p')
# print(paras)

#GEt the anchor atags
anchors = soup.find_all('a')
all_links =set()
#get all the links on the page
for link in anchors:
    if (link.get('href') !='#'):
        linkText = 'https://codewithharry.com'+link.get('href')
        all_links.add(link)
        print(linkText)
# print(anchors)

#Get tha first element in the hTML page
print(soup.find('p'))

#Get classes of any element in the html page
print(soup.find('p')['class'])

#find all the elements with class lead
print(soup.find_all('p',class_='lead'))


#Get the text from the tags/soup
print(soup.find('p').get_text())


# markup="<p> <!-- this is a comment --></p>"
# soup2= BeautifulSoup(markup)
# print(soup2.p)
# exit()

navbarSupportedContent = soup. find(id= 'navbarSupportedContent')
 # .contents - A tag's children are available as a list
 # .children - A tag's children are available as a generator//(fast)
# for elem in navbarSupportedContent. contents:
#      print(elem)
#for item in navbarSupportedContent.strings:
#     print(item)
# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# print(navbarSupportedContent.parent)

# for item in (navbarSupportedContent.parent):
#     print(item)
# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarsupportedContent.previous_sibling.previous_sibling)

elem = soup.select('#loginModal')
print(elem)