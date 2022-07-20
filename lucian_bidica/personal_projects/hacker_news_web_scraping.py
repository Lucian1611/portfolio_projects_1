import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/")
res2 = requests.get("https://news.ycombinator.com/news?p=2")
# print(res.text)
variabila = BeautifulSoup(res.text, "html.parser")
variabila2 = BeautifulSoup(res2.text, "html.parser")

links = variabila.select(".titlelink")
subtext = variabila.select(".subtext")

links2 = variabila2.select(".titlelink")
subtext2 = variabila2.select(".subtext")

mega_links = links +links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(list_hn):
   return sorted(list_hn, key=lambda k: k["votes"], reverse = True)


def create_custom_hakernews(links, subtext):
   list_hn = []
   for index, item in enumerate(links):
       title = links[index].getText()
       href = links[index].get("href", None)
       vote = subtext[index].select(".score")
       if len(vote):
           points = int(vote[0].getText().replace(" points", ""))
           if points > 99:
               list_hn.append({"title": title, "link": href, "votes": points})
   return sort_stories_by_votes(list_hn)


pprint.pprint(create_custom_hakernews(mega_links, mega_subtext))

