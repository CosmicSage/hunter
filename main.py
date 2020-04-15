#!/usr/bin/env python3.6
global CONST
CONST = "https://internshala.com"
import requests, sys, time

def incentives(meta):
    if '+' in meta: return meta[meta.index('+') + 1]
    return ''

def compare(range, price):
    try:
        if len(range) == 1 and price <= int(range[0]): return True
        elif price <= int(range[0]) or price <= int(range[1]): return True
    except Exception as e: return False

# Take User Input
mode = input("Enter Mode:")
price = int(input("Enter Lower Limit:"))
location = input("Enter Location:")
type = f"internship-in-{location}"
if mode :
    mode = "work-from-home-"
    type = "jobs"

if not price : price = 5000

for i in range(25):
    try:
        URL = f"{CONST}/internships/{mode}computer%20science-{type}/page-{i+1}"
        print(f"{URL}\n{i}\n")

        r = requests.get(URL)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(r.text, "html5lib")
        internships = soup.find_all(class_='individual_internship')

        for internship in internships:
            meta = internship.find(class_="stipend_container_table_cell").text.split()
            range = meta[0].split('-')

            if compare(range, price):
                name = internship.find(class_="link_display_like_text").text.split()
                link = CONST + internship.find(class_="view_detail_button")["href"]
                print(name, link, incentives(meta), range)

    except Exception as e:
        from datetime import datetime
        with open('./logs/error.log', 'a') as target:
            target.write(f"{datetime.now().strftime('%H:%M:%S %b %d, %Y')}\n{internship}:{name}\n")
exit(0)
"""
from the block of internships:
    Take details link if : if stipend exxecds or equals lower-limit
"""
