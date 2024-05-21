import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://roadmap.sh/python")
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title.text)
print(soup.h1.text)

with open("scrapedFile.csv", "w", newline='', encoding='utf-8') as scraped_file:
    writer = csv.writer(scraped_file)

    # Write headers to the CSV file
    writer.writerow(["Tag", "Content"])

    writer.writerow(["title", soup.title.text])
    writer.writerow(["h1", soup.h1.text])