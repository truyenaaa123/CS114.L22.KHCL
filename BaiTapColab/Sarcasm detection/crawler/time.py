from bs4 import BeautifulSoup
import json

headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}#Sửa lỗi 403
def get_fromPage(pagenumber,url):
    url_page = url + str(pagenumber)
    response = requests.get(url_page,headers=headers)
    soupSite = BeautifulSoup(response.text, 'html.parser')
    titles=soupSite.findAll('h3',class_="headline heading-3 heading-content-small padding-4-top margin-8-bottom media-heading")
    for i  in titles:
      headline = i.getText().strip().replace("\n","")
      article_link = 'https://time.com'+i.find('a')['href']
      dic ={ 
      "article_link" : article_link, "headline" : headline, "is_sarcastic" :0  } 
      with open('time.json', 'a',encoding="utf-8") as myfile:
        myfile.writelines(json.dumps(dic)+"\n")
    
def getFrom_URL(url,nb_page):
  while nb_page:
        get_fromPage(nb_page,url)
        nb_page -= 1


def main():
    URL=['https://time.com/section/us/?page=',
         'https://time.com/section/health/?page='
         'https://time.com/section/sports/?page='] 
    for i in range(len(URL)):
      if i ==0:
        getFrom_URL(URL[0],400)
      if i==1:
        getFrom_URL(URL[1],300)
      if i==2:
        getFrom_URL(URL[1],130)
      
main()