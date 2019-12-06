#!/usr/bin/env python3.6
global CONST
CONST = "https://internshala.com"
import requests, sys, time

# Take User Input
mode = input("Enter Mode:")
price = int(input("Enter Lower Limit:"))
location = input("Enter Location:")
type = f"internship-in-{location}"
if mode :
    mode = "work-from-home-"
    type = "jobs"

if not price : price = 5000

try:
    for i in range(25):
        URL = f"{CONST}/internships/{mode}computer%20science-{type}/page-{i+1}"
        # print(f"\n\n{URL}\n\n")
        r = requests.get(URL)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(r.text, "html5lib")
        internships = soup.find_all(class_='individual_internship')
        for internship in internships:
            meta = internship.find(class_="stipend_container_table_cell").text.split()
            range = meta[0].split('-')
            try:
                money = int(range[0])
            except Exception as e:
                money  = 0

            if price <= money:
                name = internship.find(class_="link_display_like_text").text.split()
                link = CONST + internship.find(class_="view_detail_button")["href"]
                print(name, link, range)

except Exception as e:
    print("No More Pages Left. Exiting....")
    exit(0)

"""
from the block of internships:
    Take details link if : if stipend exxecds or equals lower-limit
"""
