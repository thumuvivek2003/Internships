import requests
from bs4 import BeautifulSoup
mnames = []
murls = []
mprices = []
mratings  = []
mreviews = []
for i in range(1,20):
    url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2 C283&ref=sr_pg_"+str(i)
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.content,"html.parser")

    links = soup.select("h2 > a.s-link-style")

    urls = [i.get("href") for i in links]

    names = soup.select("span.a-size-medium.a-color-base.a-text-normal")
    names = [i.text for i in names]

    prices = soup.select("span.a-offscreen")
    prices = [i.text for i in prices]

    ratings = soup.select("span.a-icon-alt")
    ratings = [i.text for i in ratings]

    reviews = soup.select("span.a-size-base.s-underline-text")
    reviews = [i.text for i in reviews]

    for i in urls:murls.append(i)
    for i in names:mnames.append(i)
    for i in prices:mprices.append(i)
    for i in ratings:mratings.append(i)
    for i in reviews:mreviews.append(i)

#Names : <span class="a-size-medium a-color-base a-text-normal">SAFARI 15 Ltrs Sea Blue Casual/School/College Backpack (DAYPACKNEO15CBSEB)</span>
#Links : <a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" target="_blank" href="/American-Tourister-AMT-SCH-02/dp/B07CJCGM1M/ref=sr_1_1?crid=2M096C61O4MLT&amp;keywords=bags&amp;qid=1679310176&amp;refinements=p_n_availability%3A1318485031&amp;rnid=1318483031&amp;sprefix=ba%2Caps%252+C283&amp;sr=8-1"><span class="a-size-medium a-color-base a-text-normal">American Tourister 32 Ltrs Black Casual Backpack (AMT FIZZ SCH BAG 02 - BLACK)</span> </a>
#Prices : <span class="a-offscreen">₹849</span>
#Rating : <span class="a-icon-alt">3.9 out of 5 stars</span>
#Number of Reviews : <span class="a-size-base s-underline-text">(2,331)</span>

data = [murls,mnames,mprices,mratings,mreviews]
transpose = [list(row) for row in zip(*data)]
head = ["URLS","NAMES","PRICES","RATINGS","REVIEWS"]
transpose.insert(0,head)
#Converting into CSV File
import csv
with open("data.csv","w",newline="",encoding="utf-8") as data:
    writer = csv.writer(data,delimiter=",")
    for row in transpose:
        writer.writerow(row)
        print(row)