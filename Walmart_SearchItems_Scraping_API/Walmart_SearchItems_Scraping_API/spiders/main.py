import scrapy
from scrapy import Request
import json
import logging


class MainSpider(scrapy.Spider):
    name = "main"
    logging.basicConfig(
        filename="Logfile.log",
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode='w',
        level=logging.ERROR,
    )

    """
    Using page url then find the hidden API/Json in page source
    """
    url = 'https://www.walmart.com/search?q=automatic+espresso+machine&affinityOverride=default&page={}'

    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52",
    }

    def start_requests(self):
        for i in range(1, 26):
            try:
                print('\n')
                print('PAGE {}'.format(i))
                print('\n')
                request = Request(
                        url=self.url.format(i),
                        # url=self.url,
                        headers=self.headers,
                        callback=self.parse
                )
                yield request
            except Exception as e:
                self.logger.error("Page {} has error {}".format(i, e))

    def parse(self, response):
        """
        Hidden API/Json in page source/element
        Easier to paginate using this method compare to API in network tool
        """
        body_data = response.css('script[id="__NEXT_DATA__"]::text').get()
        raw_data = json.loads(body_data)

        """
        Dumping the nested json object into text
        Using the [Jsonpathfinder]('https://jsonpathfinder.com/')
        to find the path of the nested data

        Below is the code to dump json object
        """
        # with open("walmart_raw.json", "w") as outfile:
        #     json.dump(raw_data, outfile, indent=4, sort_keys=True)

        data = raw_data['props']['pageProps']['initialData']['searchResult']['itemStacks'][0]['items']
        for x in range(len(data)):
            try:
                print('\n')
                print('Item {}'.format(x))
                print('\n')
                items = {
                    'Name': data[x]['name'],
                    'Price': data[x]['price'],
                    'Availability': data[x]['availabilityStatusDisplayValue'],
                    'Url Link': 'https://www.walmart.com'+data[x]['canonicalUrl'],
                }
                yield items
            except Exception as e:
                # logger.debug("Item {} has {}".format(x, e))
                self.logger.error("Item {} has error {}".format(x, e))
