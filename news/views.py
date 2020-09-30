import requests
from django.shortcuts import render, redirect
from django.db import IntegrityError
from bs4 import BeautifulSoup
from .models import Content

# Create your views here.
# toi_headings = toi_soup.find_all('h2')
# Content Aggregating From Gundrukpost
toi_r = requests.get("http://www.gundrukpost.com/")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')
toi_headings = toi_soup.findAll("h2", {"class": "entry-title format-icon"})[0:9]
toi_category = toi_soup.findAll("a", {"class": ""})[0:9]
toi_news = [th.text for th in toi_headings]
toi_cat = [tr.text for tr in toi_category]

for th in toi_headings:
    toi_news.append(th.text)

for tr in toi_category:
    toi_cat.append(tr.text)

#storing scrape data in table Content
for title, category in zip(toi_news, toi_cat):
    try:
        n = Content.objects.create(title=title, category=category)
    except IntegrityError as e:
        if 'unique constraint' in e.args:
            continue


# Content Aggregating From lexlimbu.com
loi_r = requests.get("https://lexlimbu.com/")
loi_soup = BeautifulSoup(loi_r.content, 'html5lib')
loi_headings = loi_soup.findAll("h3", {"class": "entry-title td-module-title"})[0:9]
loi_category = loi_soup.findAll("a", {"class": "td-post-category"})[0:9]
loi_news = [lh.text for lh in loi_headings]
loi_cat = [lr.text for lr in loi_category]

for lh in loi_headings:
    loi_news.append(lh.text)

for lr in loi_category:
    loi_cat.append(lr.text)

#storing scrape date in table Content
for title, category in zip(loi_news, loi_cat):
    try:
        n = Content.objects.create(title=title, category=category)
    except IntegrityError as e:
        if 'unique constraint' in e.args:
            continue


# a normal view to check the data is being received or not

def index(request):
    return render(request,'index.html',{'toi_news':toi_news, 'toi_cat': toi_cat,'loi_news': loi_news,'loi_cat': loi_cat,})



# def scrape(request):
#     session = requests.Session()
#     session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
#     url = "https://www.mashable.com/"
#
#     content = session.get(url, verify=False).content
#     soup = BSoup(content, "html.parser")
#     News = soup.find_all('div', {"class": "article-container sharable"})
#     for n in News:
#         main = n.find_all('a')[0]
#         link = main['href']
#         image_src = str(main.find('img')['srcset']).split(" ")[-4]
#         title = main['title']
#         cat = main['title']
#         new_content = Content()
#         new_content.title = title
#         new_content.url = link
#         new_content.image = image_src
#         new_content.category = cat
#         new_content.save()
#     return redirect("../")






