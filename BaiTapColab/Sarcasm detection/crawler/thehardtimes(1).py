from bs4 import BeautifulSoup
import json

headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}#Sửa lỗi 403
def get_fromPage(pagenumber,url):
    url_page = url + str(pagenumber)
    response = requests.get(urlPage,headers=headers)
    soupSite = BeautifulSoup(response.text, 'html.parser')
    titles = soupSite.findAll('h2',class_="post-title")
    for i  in titles:
      headline = i.find('a').getText().replace("\n","")
      article_link = i.find("a")['href']
      dic ={ 
      "article_link" : article_link, "headline" : headline, "is_sarcastic" :1  } 
      with open('thehardtimes.json', 'a',encoding="utf-8") as myfile:
        myfile.writelines(json.dumps(dic)+"\n")
    
def getFrom_URL(url,nb_page):
  while nb_page:
        get_fromPage(nb_page,url)
        nb_page -= 1


def main():
    URL=['https://thehardtimes.net/page/','https://thehardtimes.net/news/page/','https://thehardtimes.net/blog/page/',
         'https://thehardtimes.net/music/page/'] 
    for i in range(len(URL)):
      if i ==0:
        getArticleFrom_URL(URL[0],300)
      if i==1:
        getArticleFrom_URL(URL[1],53)
      if i==2:
        getArticleFrom_URL(URL[2],105)
      if i==3:
        getArticleFrom_URL(URL[3],187)
    
main()