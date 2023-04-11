import requests  # allows to download the html from websites
from bs4 import BeautifulSoup  # allows to scrape (clean up the .txt)
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.titleline > a')
links2 = soup2.select('.titleline > a')

subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def custom_hn(links, subtext):
    hn = []
    for idx, i in enumerate(links):
        title = i.getText()
        href = i.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories(hn)


pprint.pprint(custom_hn(mega_links, mega_subtext))
