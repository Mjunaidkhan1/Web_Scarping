import requests
from bs4 import BeautifulSoup


url='https://foloswap.com/'

r=requests.get(url)
htmlContent=r.content

# print(htmlContent)

################################
##### for Prettify Data ########
################################


testSoup =BeautifulSoup(htmlContent,'html.parser')
# print(testSoup.prettify())

################################
##### Get selected Data ########
################################

title=testSoup.title
# title=testSoup.title.string
# print(title)

# print(type(testSoup))
# print(type(title))
# print(type(title.string))

###############################
##### Get all any teg  ########
###############################

para = testSoup.find_all('div')
# print(para)

################################################
##### Get first Tag any sellected teg   ########
################################################

div = testSoup.find('div')
# print(div)

############################################################
##### Get first Tag all classes any sellected teg   ########
############################################################

div = testSoup.find('div')['class']
# print(div)

###################################################################
##### Get all sellected tags which have sellected classe   ########
###################################################################

div = testSoup.find_all('i',class_="fa-angle-up" )
# print(div)

#####################################################
##### Get first Tag Text any sellected teg   ########
#####################################################

div = testSoup.find('p').get_text()
# print(div)

#############################
##### Get all text   ########
#############################

div = testSoup.get_text()
# print(div)

#######################################
##### Get all link in <a> tags ########
#######################################

atag = testSoup.find_all('a')
for i in atag:
 if (i.get('href') !='#'):
          link ='https://foloswap.com'+i.get('href')
          # print(link)

####################################################
##### Get first tag by a class and its func ########
####################################################

div = testSoup.find('div',class_="menu")
# for i in div.contents:
#   print(i)
# for i in div.children:
#   print(i)
# for i in div.strings:
#   print(i)
# for i in div.stripped_strings:
#   print(i)
# for i in div.parents:
#   print(i.name)
# print(div.parent)
# print(div.previous_sibling.previous_sibling)
# print(div.next_sibling.next_sibling)


###################################
##### Get from id or class ########
###################################
# print(testSoup.select('.opener'))