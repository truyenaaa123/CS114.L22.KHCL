from bs4 import BeautifulSoup
import json

headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}#Sửa lỗi 403
def get_fromPage(pagenumber,url):
    url_page = url + str(pagenumber)
    response = requests.get('https://chaser.com.au/news/page/40',headers=headers)
    soupSite = BeautifulSoup(response.text, 'html.parser')
    titles1 = soupSite.find('div',id="archive_posts")
    titles_link=titles1.findAll("a")
    titles3=titles1.findAll('div',class_='archive_story_title')
    for i in range(len(titles3)):
      headline = titles3[i].getText().replace("\n","")
      #headline= headline.getText()
      article_link = titles_link[i]['href']
      dic ={ 
      "article_link" : article_link, "headline" : headline, "is_sarcastic" :1  } 
      with open('chaser.json', 'a',encoding="utf-8") as myfile:
        myfile.writelines(json.dumps(dic)+"\n")
    
def getFrom_URL(url,nb_page):
  while nb_page:
        get_fromPage(nb_page,url)
        nb_page -= 1


def main():
    URL=['https://chaser.com.au/news/page/',]
    getFrom_URL(URL[0],160)
    
main()