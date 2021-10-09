import scrapy

def get_weburls():
    
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    
    states = [x.lower() for x in states]
    
    urls = []
    page = "https://www.plannedparenthood.org/health-center/"
    for state in states:
        s = page + state
        urls.append(s)
    return urls

class ClinicsScraper(scrapy.Spider):
    name = "scrapper"

    def  start_requests(self):
        urls = get_weburls()

        # from the base urls, extract the next urls to call
        for url in urls:
            yield scrapy.Request(url=url, callback=self.postParse)
    
    def postParse(self, response):
        
        base = "https://www.plannedparenthood.org"
        
        # call all the possible urls and download the content from each one of them.
        for weblink in response.xpath('*//a/@href').extract():
            if weblink.startswith("/clinics/"):
                yield {"weblink" : base + weblink}
            




