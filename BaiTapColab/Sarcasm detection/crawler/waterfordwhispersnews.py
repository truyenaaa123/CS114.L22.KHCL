from bs4 import BeautifulSoup
import json

headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}#Sửa lỗi 403
def get_fromPage(pagenumber,url):
    url_page = url + str(pagenumber)
    response = requests.get(url_page,headers=headers)
    soupSite = BeautifulSoup(response.text, 'html.parser')
    titles1 = soupSite.find('div',id="main")
    titles2=titles1.findAll('article')
    for i  in titles2:
      headline = i.find('a').getText().replace("\n","")
      article_link = i.find("a")['href']
      dic ={ 
      "article_link" : article_link, "headline" : headline, "is_sarcastic" :1  } 
      with open('waterfordwhispersnews.json', 'a',encoding="utf-8") as myfile:
        myfile.writelines(json.dumps(dic)+"\n")
    
def getFrom_URL(url,nb_page):
  while nb_page:
        get_fromPage(nb_page,url)
        nb_page -= 1


def main():
    URL=['https://waterfordwhispersnews.com/category/breaking-news/page/',
         'https://waterfordwhispersnews.com/category/lifestyle/page/',
         'https://waterfordwhispersnews.com/category/politics/page/',
         'https://waterfordwhispersnews.com/category/entertainment/page/'] 
    for i in range(len(URL)):
      if i ==0:
        getFrom_URL(URL[0],425)
      if i==1:
        getFrom_URL(URL[1],35)
      if i==2:
        getFrom_URL(URL[2],110)
      if i==3:
       getFrom_URL(URL[3],40)
    
main()