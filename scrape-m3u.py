#!/usr/bin/env python3
import os
import requests
from bs4 import BeautifulSoup
import re


#Create a directory where all the scraped .m3u files will be stored
os.makedirs("./scraped-m3us", exist_ok = True)
#Enter URL where you can find all the m3u links
URL = input("Enter your URL: ")


page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

#Find all the m3u links on the page
link_list = soup.findAll(string=re.compile(r'^http.*m3u$'))

i = 0

#Main function that collects all the m3u data from the links found in "link_list"
for link in link_list:
    try:
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        print("---")
        print(link)
        if "<" in str(soup):
            print("Contains tag in request (probably, 403 error!), couldn't be written to file!")
        else:
            with open(f"./scraped-m3us/myfile_{i}.m3u", "w") as file1:
                file1.writelines(soup)
                print("---")
                print("\n")
        i+=1
    except requests.exceptions.ConnectionError:
        print("---")
        print(link)
        print('Request has timed out!')
        print("---")
        print("\n")

os.system("clear")
print("Finished!")
