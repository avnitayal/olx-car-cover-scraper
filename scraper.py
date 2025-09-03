import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.olx.in/items/q-car-cover"

r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(r.text, "html.parser")

ads = soup.find_all("li", {"data-aut-id": "itemBox"})

with open("car_covers.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Location", "URL"])

    for ad in ads:
        title = ad.find("span", {"data-aut-id": "itemTitle"})
        price = ad.find("span", {"data-aut-id": "itemPrice"})
        location = ad.find("span", {"data-aut-id": "itemLocation"})
        link = ad.find("a")

        writer.writerow([
            title.text if title else "",
            price.text if price else "",
            location.text if location else "",
            "https://www.olx.in" + link["href"] if link else ""
        ])

print("Results saved to car_covers.csv")
