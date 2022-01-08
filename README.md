# Goal
Many Hiring Platforms (Ex. Indeed, Intershala, Stackoverflow) Dont allow filtering results by the aspects like :
1. Salary/Stipend(For interships)

Therefore I made this extremely simple scraping tool that allows one find relevant jobs. Unfortunately The day these websites change their DOM structure this tool will need an update

At This Point It only supports Intershala.com. In future I'll add more websites

![Image of a Hunter](https://cdn.gamer-network.net/2020/metabomb/sova-ultimate.jpg)
<p align="center"><sub>(hate the game but the character is cools)</sub></p>

## Installation
You will need python and pip. Install dependencies with:
```bash
pip3 install --trusted-host pypi.python.org -r requirements.txt
```

## Usage
Pretty darn simple :
```bash
cd hunter; mkdir logs; python3 main.py
```

Then one must enter whether they want a remote job or all jobs & also set The Lower Limit of Salary


## Future
Add More Websites & A SQLite Database to keep track of which jobs you have already applied for + GUI
