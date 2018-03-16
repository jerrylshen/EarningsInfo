from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

tickers_input = input("Please enter tickers: ")
tickers = []

for e in tickers_input.split():
    tickers.append(e)

base_url = "https://www.nasdaq.com/earnings/report/"

data_list = []
for ticker in tickers:
    open_page = urlopen(base_url+ticker)
    soup = BeautifulSoup(open_page, "html.parser")
    name_box = soup.find("h2")
    detail_box = soup.find("span", attrs={"id": "two_column_main_content_reportdata"})

    name = name_box.text.strip()
    detail = detail_box.text.strip()
    data_list.append([name, detail])

row = 0
col = 0
for e in data_list:
    file = open("stocks", "a")
    eps = re.search(r"\b(consensus)\b", str(e[1]))
    try:
        first_index = eps.start()
        string = str(e[0]) + "\n" + str(e[1][first_index::]) + "\n"*2
        file.write(string)
    except:
        print(e[0] + " hasn't released an earnings report date yet")
    file.close()


