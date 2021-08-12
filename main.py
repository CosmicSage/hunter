#!/usr/bin/env python3.6
global CONST
CONST = "https://internshala.com"
import requests, sys, time
from bs4 import BeautifulSoup

# if want_file: generate_file(name, link, incentives(meta), range)
def generate_file(blocks):
    with open("./result.html", 'r+') as target:
        root = BeautifulSoup(target, "html5lib").find(id="root")
        root.clear()
        for name, link, incentives, range in blocks:
            tag = BeautifulSoup(f"""
                <div>
                    <h1>{' '.join(name)}</h1>
                    <h2>Reward: {'-'.join(range)} {incentives}</h2>
                    <h3><a href={link}>Apply</a></h3>
                </div>
                """, "html5lib")
            root.append(tag)

        # root.children = []
        # print(root)
# generate_file()
# exit()

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
price = input("Enter Lower Limit:")
location = input("Enter Location:")
keyword = input("Any Keyword?:")
want_file = input("Generate File?(Press Enter for NO):")
type = f"internship-in-{location}"

if mode :
    mode = "work-from-home-"
    type = "jobs"

if not price : price = 5000
blocks = []
for i in range(3):
    try:
        if not keyword: URL = f"{CONST}/internships/{mode}computer%20science-{type}/page-{i+1}"
        else: URL = F"{CONST}/internships/keywords-{keyword}/page-{i+1}"
        print(f"{URL}\n{i}\n")

        r, meta = requests.get(URL), ""
        soup = BeautifulSoup(r.text, "html5lib")
        internships = soup.find_all(class_='individual_internship')
        if len(internships) == 2: sys.exit("No more results left")

        for internship in internships:
            meta = internship.find(class_="stipend").text.split()
            range = meta[0].split('-')

            if compare(range, int(price)):
                name = internship.find(class_="link_display_like_text").text.split()
                link = CONST + internship.find(class_="view_detail_button")["href"]
                if want_file: blocks.append((name, link, incentives(meta), range))
                print(name, link, incentives(meta), range)

    except AttributeError as e:
        print(e)
        # info = name if name is not None else meta
        with open('./logs/error.log', 'a') as target:
            from datetime import datetime
            target.write(f"{datetime.now().strftime('%H:%M:%S %b %d, %Y')}\n{internship}:{meta}\n")
        if "not find" in internship.find(class_="heading_6").text: exit("Maximum pages searched")

if want_file:
    generate_file(blocks)
exit(0)
"""
from the block of internships:
    Take details link if : if stipend exxecds or equals lower-limit
"""
