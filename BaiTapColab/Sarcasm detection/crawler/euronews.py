from bs4 import BeautifulSoup
import json
headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}#Sửa lỗi 403
def get_From_Page(pagenumber,url):
    urlPage = url + str(pagenumber)
    response = requests.get(urlPage,headers=headers)
    soupSite = BeautifulSoup(response.text, 'html.parser')
    titles = soup.findAll('h3',class_="m-object__title qa-article-title")
    for i  in titles:
      headline = i.find("a")['title']
      article_link = 'https://www.euronews.com'+i.find("a")['href']
      dic ={ 
      "article_link" : article_link, "headline" : headline, "is_sarcastic" :0  } 
      with open('euronews.json', 'a',encoding="utf-8") as myfile:
        myfile.writelines(json.dumps(dic)+"\n")
    
def get_From_URL(url,nb_page):
  while nb_page:
        get_From_Page(nb_page,url)
        nb_page -= 1


def main():
    URL=['https://www.euronews.com/tag/united-kingdom?p=','https://www.euronews.com/news/asia?p='] 
    for i in range(len(URL)):
      if i ==0:
        get_From_URL(URL[0],142)
      else:
        get_From_URL(URL[1],450)
    
main()