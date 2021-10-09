import scrapy, json

def get_weburls():
    file = "clinics.json"
    urls = []
    with open(file) as f:
        weblinks = json.load(f)
    for i in range(len(weblinks)):
        weblink = weblinks[i]["weblink"]
        urls.append(weblink)
    return urls

class ClinicsScraper(scrapy.Spider):
    name = "address_scrapper"

    def  start_requests(self):
        urls = get_weburls()

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):

        for post in response.xpath('//p[@class="address-loc"]'):
            
            address = post.xpath('//span[@itemprop="streetAddress"]/text()').get()
            city = post.xpath('//span[@itemprop="addressCity"]/text()').get()
            state = post.xpath('//span[@itemprop="addressState"]/text()').get()
            zipcode = post.xpath('//span[@itemprop="zipcode"]/text()').get()
            
            yield {"address" : address,
                   "city": city,
                   "state"  : state,
                   "zipcode"  : zipcode} 
            

with open("addresses.json") as f:
    data = json.load(f)

import csv
with open('clinics.csv', 'w', newline='') as csvfile:
    fieldnames = ["address", "city", "state", "zipcode"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)
