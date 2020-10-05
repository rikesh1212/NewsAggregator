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


# scraping data from nepalnews.com
noi_r = requests.get("https://www.nepalnews.com/")
noi_soup = BeautifulSoup(noi_r.content,'html5lib')
noi_headings = noi_soup.findAll("a", {"class": "uk-link-reset"})[0:9]
noi_category = noi_soup.findAll("span", {"class": "uk-button uk-button-secondary uk-button-small"})[0:9]
noi_news = [nh.text for nh in noi_headings]
noi_cat = [nr.text for nr in noi_category]

for nh in noi_headings:
    noi_news.append(nh.text)

for nr in noi_category:
    noi_cat.append(nr.text)

for title, category in zip(noi_news, noi_cat):
    try:
        n = Content.objects.create(title=title, category=category)
    except IntegrityError as e:
        if 'unique constraint' in e.args:
            continue


poi_r = requests.get("https://www.ashesh.com.np/category/news/")
poi_soup = BeautifulSoup(poi_r.content,'html5lib')
poi_headings = poi_soup.findAll("h2", {"class": "title"})[0:9]
poi_category = poi_soup.findAll("div", {"class": "featured-cat"})[0:9]
poi_news = []
poi_cat = []

for ph in poi_headings:
    poi_news.append(ph.text)

for pr in poi_category:
    poi_cat.append(pr.text)

for title, category in zip(poi_news, poi_cat):
    try:
        n = Content.objects.create(title=title, category=category)
    except IntegrityError as e:
        if 'unique constraint' in e.args:
            continue









