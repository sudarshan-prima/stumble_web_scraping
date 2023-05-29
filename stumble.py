from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import requests
from bs4 import BeautifulSoup
import getDriver


# def get_database():
#     CONNECTION_STRING = "mongodb+srv://user1:cLBNmZmIaAoiAABT@cluster-google-play-scr.mnbryjj.mongodb.net/test?connectTimeoutMS=60000"
#     from pymongo import MongoClient
#     client = MongoClient(CONNECTION_STRING)
#
#     return client['test']


url = 'http://www.stumble.studio/categories/?category=Sustainable'
# requests.get(url)
getDriver.get_driver().get(url)
sleep(5)
#
# dbname = get_database()
# collection_name = dbname["stumble_data"]

datas = getDriver.get_driver().find_elements(By.CLASS_NAME, 'card')

titleUrl = '/html/body/div/div[{}]/div/div[2]/div/h4/a'
descriptionUrl = '/html/body/div/div[{}]/div/div[2]/div/div/p'
tagsUrl = '/html/body/div/div[{}]/div/div[2]/div/p'
pageUrl = '/html/body/div/div[{}]/div/div[2]/div/a[1]'

links = []
title = []
description = []
tags = []
products = []
founders = []
headquarters = []
instagramLink = []
facebookLink = []
linkedInLink = []
websiteLink = []
category = []

for i, data in enumerate(datas):
    title.append(data.find_element(By.XPATH, titleUrl.format(i + 1)).text)
    try:
        description.append(data.find_element(By.XPATH, descriptionUrl.format(i + 1)).text)
    except Exception as Ex:
        description.append('')
    getTags = data.find_elements(By.XPATH, tagsUrl.format(i + 1))
    getPageLink = data.find_element(By.XPATH, pageUrl.format(i + 1)).get_attribute('href')
    pageDetails = requests.get(getPageLink)

    soup = BeautifulSoup(pageDetails.content, features="lxml")
    product = soup.select_one('body > div > div:nth-child(3) > div > p:nth-child(1)').get_text()
    products.append(product)

    try:
        founder = soup.select_one('body > div > div:nth-child(3) > div > p:nth-child(2)').get_text()
        founders.append(founder)
    except Exception as Ex:
        founders.append('')

    try:
        headquarter = soup.select_one('body > div > div:nth-child(3) > div > p:nth-child(3)').get_text()
        headquarters.append(headquarter)
    except Exception as Ex:
        headquarters.append('')

    try:
        instagram = soup.select_one('body > div > div:nth-child(3) > div > ul > li:nth-child(1) > a').attrs['href']
        instagramLink.append(instagram)
    except Exception as Ex:
        instagramLink.append('')

    try:
        facebook = soup.select_one('body > div > div:nth-child(3) > div > ul > li:nth-child(2) > a').attrs['href']
        facebookLink.append(facebook)
    except Exception as Ex:
        facebookLink.append('')

    try:
        linkedIn = soup.select_one('body > div > div:nth-child(3) > div > ul > li:nth-child(3) > a').attrs['href']
        linkedInLink.append(linkedIn)
    except Exception as Ex:
        linkedInLink.append('')

    try:
        website = soup.select_one('body > div > div:nth-child(3) > div > ul > li:nth-child(4) > a').attrs['href']
        websiteLink.append(website)
    except Exception as Ex:
        websiteLink.append('')

    for getTag in getTags:
        tags.append(getTag.find_element(By.TAG_NAME, 'small').text)

    try:
        data.find_element(By.CLASS_NAME, 'btn-warning')
        link = data.find_element(By.CLASS_NAME, 'btn-warning').get_attribute('href')
        links.append(link)
    except Exception as Ex:
        links.append("")

    category.append('Sustainable')

# getDriver.get_driver().quit()
#
datafile = pd.DataFrame({'title': title, 'description': description, 'tags': tags, 'links': links, 'products': products,
                         'founders': founders, 'headquarters': headquarters, 'instagramLink': instagramLink,
                         'facebookLink': facebookLink, 'linkedInLink': linkedInLink, 'websiteLink': websiteLink, 'category': category})
# datafile.to_csv('health.csv', index=False)
insertData = datafile.to_dict(orient='records')
# collection_name.insert_many(insertData)
print(title, 'title', len(title))
#
# '/html/body/div/section[1]/div/div/div[2]/div[{}]/a'
# '/html/body/div/section[1]/div/div/div[2]/div[2]/a'
# '/html/body/div/section[1]/div/div/div[2]/div[3]/a'
