import re
import urllib
from bs4 import BeautifulSoup
import sys


url = raw_input("Enter the url\n\n")
#media =raw_input("Enter the social media")

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

if(re.findall('\\binstagram\\b',url)):
    description = soup.find('meta',{"property":"og:description"})
    url = soup.find('meta',{"property":"og:url"})
    print description.get('content')
    print url.get('content')
    sys.exit()

if(re.findall('\\bplay\\b',url)):
    titlevideo = soup.find('div',{"jsname":"C4s9Ed"})
    description= ''.join(titlevideo.text)
    sentences = description.split('\n')
    print sentences[0]
    sys.exit()
    #print description

if(re.findall('\\byoutube\\b',url)):
    titlevideo = soup.find('meta',{"property":"og:title"})
    print ("--------------Video Title----------------")
    print("")
    print ''.join(titlevideo.get('content'))
    print("")
    uploadinfo = soup.find('div',{"id":"watch-uploader-info"}).strong.contents
    print ("--------------Published On----------------")
    print("")
    #print uploadinfo
    print ''.join(uploadinfo)

    print("")

    #description = soup.find('div',{"id":"watch-description-text"}).p.contents
    description = soup.find('p',{"id":"eow-description"})
    print ("--------------Video Description----------------")
    print("")
    a1=''.join([unicode(i) for i in description])
    a2=BeautifulSoup(a1,"html.parser") 
    string_for_output = a2.text
    stringout = string_for_output.encode('utf8')
    print stringout


    print("")
    category = soup.find_all('li',{"class":"watch-meta-item yt-uix-expander-body"})

    for i in range(len(category)):

        first_cat_name=''.join(category[i].h4.contents)
        print first_cat_name
        first_desc_name=''.join(category[i].ul.li.text)
        print first_desc_name


    sys.exit()

if(re.findall('\\bpinterest\\b',url)):
    titlevideo = soup.find('meta',{"property":"og:description"})
    description= ''.join(titlevideo.get('content'))
    print description
    sys.exit()

else:
    print("Enter the correct url")
