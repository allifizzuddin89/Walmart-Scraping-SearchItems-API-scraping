import scrapy
from scrapy import Request
import json
# from scrapy.shell import inspect_response


class MainSpider(scrapy.Spider):
    name = "main"

    url = 'https://www.walmart.com/orchestra/snb/graphql/Search/0d430070b29087d0816fdde9b3007bc0d6142d39a2537d8a1fd02cb005ea23f8/search?variables=%7B%22id%22%3A%22%22%2C%22affinityOverride%22%3A%22default%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22automatic%20espresso%20machine%22%2C%22page%22%3A1%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%22%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22automatic%20espresso%20machine%22%2C%22cat_id%22%3A%22%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22fitmentFieldParams%22%3A%7B%22powerSportEnabled%22%3Atrue%7D%2C%22fitmentSearchParams%22%3A%7B%22id%22%3A%22%22%2C%22affinityOverride%22%3A%22default%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22automatic%20espresso%20machine%22%2C%22page%22%3A1%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%22%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22automatic%20espresso%20machine%22%2C%22cat_id%22%3A%22%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22cat_id%22%3A%22%22%2C%22_be_shelf_id%22%3A%22%22%7D%2C%22enableFashionTopNav%22%3Afalse%2C%22enablePortableFacets%22%3Atrue%2C%22enableFacetCount%22%3Atrue%2C%22fetchMarquee%22%3Atrue%2C%22fetchSkyline%22%3Atrue%2C%22fetchGallery%22%3Afalse%2C%22fetchSbaTop%22%3Atrue%2C%22tenant%22%3A%22WM_GLASS%22%2C%22enableFlattenedFitment%22%3Afalse%2C%22pageType%22%3A%22SearchPage%22%7D'

    headers = {
        "authority": "www.walmart.com",
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "device_profile_ref_id": "ANST2wyXFRjcrqVeZNG4OaBWe-q6EqmALdUl",
        "dnt": "1",
        "pragma": "no-cache",
        "referer": "https://www.walmart.com/search?q=automatic+espresso+machine&affinityOverride=default",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "traceparent": "00-ac893da9f999ac818f79a8002f1af043-bbe6c8d90bf19304-00",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52",
        "wm_mp": "true",
        "wm_page_url": "https://www.walmart.com/search?q=automatic+espresso+machine&affinityOverride=default",
        "wm_qos.correlation_id": "t88th96Oe3Ho3a4JnVpX7nrfI0-BmKL5d_a5",
        "x-apollo-operation-name": "Search",
        "x-enable-server-timing": "1",
        "x-latency-trace": "1",
        "x-o-bu": "WALMART-US",
        "x-o-ccm": "server",
        "x-o-correlation-id": "t88th96Oe3Ho3a4JnVpX7nrfI0-BmKL5d_a5",
        "x-o-gql-query": "query Search",
        "x-o-mart": "B2C",
        "x-o-platform": "rweb",
        "x-o-platform-version": "main-1.32.0-b2719e",
        "x-o-segment": "oaoh"
    }

    cookies = {
        "TBV": "7",
        "dimensionData": "969",
        "ACID": "1b48c8eb-9448-4682-96b5-71075d876a99",
        "hasACID": "true",
        "assortmentStoreId": "3081",
        "hasLocData": "1",
        "TB_Latency_Tracker_100": "1",
        "TB_Navigation_Preload_01": "1",
        "vtc": "QzDD2RBNu_FFpPmvESptGU",
        "_pxhd": "e08f4ae8cfa12004af2198bf6308f9c74a532deb02b7c55278e17fe153c2c41d:95813da6-6719-11ed-95fc-556c44645451",
        "_astc": "8654eada51a4b8611a65b8bd9517eafb",
        "AID": "wmlspartner%3D0%3Areflectorid%3D0000000000000000000000%3Alastupd%3D1668759708848",
        "locGuestData": "eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjp0cnVlLCJzdG9yZVNlbGVjdGlvblR5cGUiOiJERUZBVUxURUQiLCJwaWNrdXAiOnsibm9kZUlkIjoiMzA4MSIsInRpbWVzdGFtcCI6MTY2ODc1OTUwOTkxNX0sInNoaXBwaW5nQWRkcmVzcyI6eyJpZCI6bnVsbCwidGltZXN0YW1wIjoxNjY4NzU5NTA5OTE1LCJjcmVhdGVUaW1lc3RhbXAiOm51bGwsInR5cGUiOiJwYXJ0aWFsLWxvY2F0aW9uIiwiZ2lmdEFkZHJlc3MiOmZhbHNlLCJwb3N0YWxDb2RlIjoiOTU4MjkiLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EiLCJkZWxpdmVyeVN0b3JlTGlzdCI6W3sibm9kZUlkIjoiMzA4MSIsInR5cGUiOiJERUxJVkVSWSJ9XX0sInBvc3RhbENvZGUiOnsidGltZXN0YW1wIjoxNjY4NzU5NTA5OTE1LCJiYXNlIjoiOTU4MjkifSwibXAiOltdLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6MWI0OGM4ZWItOTQ0OC00NjgyLTk2YjUtNzEwNzVkODc2YTk5In0%3D",
        "mobileweb": "0",
        "xptc": "assortmentStoreId%2B3081",
        "xpth": "x-o-mverified%2Bfalse",
        "auth": "MTAyOTYyMDE4%2FrZGLdEd1jaAwMxBm9A2J5JMd%2Boiwh2aMuPJXSJvQan1TC0JG4xLav%2BLEX1amhH7UZ%2B0aQWjEwBedVlG6E%2FagkJ5vS5gbg8pg8CtDnvMzHlzbHOJIa7w3ilPj8%2Fbl4qV767wuZloTfhm7Wk2Kcjygv699%2F6tFVwuL3qJB39WKV9C7vKx%2BIJjKWWbDBv2CQSL8HOYILvpHH6kd1lMHfxur8SMCDQ%2FMrA%2FawAoa9%2Br8JoUMk70P8glgOEpLOprhDfMM%2FFHGZ2dCNmxWrdkwqEKrvde9h7lqxTnKoYLZk9WtAFvvOSJcPwLEjljBGQc1nPjiCiOYNxkVD1NKZ3aqV%2FrWiRG2aJbiyBXOh4XYMbPZ9sPUricqQsjWhwFeVPhzybqAHQ%2FpRwKemvNyU1TIKPKIEjyrOXbKKhH072NS%2FW0j%2FU%3D",
        "bstc": "QDbxT_sAbN-rzDmU8bbdDc",
        "xpm": "3%2B1668837213%2BQzDD2RBNu_FFpPmvESptGU~%2B0",
        "locDataV3": "eyJpc0RlZmF1bHRlZCI6dHJ1ZSwiaXNFeHBsaWNpdCI6ZmFsc2UsImludGVudCI6IlNISVBQSU5HIiwicGlja3VwIjpbeyJidUlkIjoiMCIsIm5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJub2RlVHlwZSI6IlNUT1JFIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiOTU4MjkiLCJhZGRyZXNzTGluZTEiOiI4OTE1IEdlcmJlciBSb2FkIiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5NTgyOS0wMDAwIn0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjozOC40ODI2NzcsImxvbmdpdHVkZSI6LTEyMS4zNjkwMjZ9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIzMDgxIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9JTlNUT1JFIiwiUElDS1VQX0NVUkJTSURFIl19XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjozOC40NzQ0LCJsb25naXR1ZGUiOi0xMjEuMzQzNywicG9zdGFsQ29kZSI6Ijk1ODI5IiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiY291bnRyeUNvZGUiOiJVU0EiLCJnaWZ0QWRkcmVzcyI6ZmFsc2V9LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJhY2Nlc3NQb2ludHMiOm51bGwsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbXSwiaW50ZW50IjoiUElDS1VQIiwic2NoZWR1bGVFbmFibGVkIjpmYWxzZX0sImRlbGl2ZXJ5Ijp7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMzA4MSIsImRpc3BsYXlOYW1lIjoiU2FjcmFtZW50byBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5NTgyOSIsImFkZHJlc3NMaW5lMSI6Ijg5MTUgR2VyYmVyIFJvYWQiLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6Ijk1ODI5LTAwMDAifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjM4LjQ4MjY3NywibG9uZ2l0dWRlIjotMTIxLjM2OTAyNn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOnRydWUsImFjY2Vzc1BvaW50cyI6W3siYWNjZXNzVHlwZSI6IkRFTElWRVJZX0FERFJFU1MifV0sImh1Yk5vZGVJZCI6IjMwODEiLCJpc0V4cHJlc3NEZWxpdmVyeU9ubHkiOmZhbHNlLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJERUxJVkVSWV9BRERSRVNTIl19LCJpbnN0b3JlIjpmYWxzZSwicmVmcmVzaEF0IjoxNjY4ODU4ODE1NjMxLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6MWI0OGM4ZWItOTQ0OC00NjgyLTk2YjUtNzEwNzVkODc2YTk5In0%3D",
        "bm_mi": "F8D9BF9EC73672F281493512C1A3BE11~YAAQEqwwF7WD+XmEAQAAtrpzjhGAy/84NGsfiLXxVyRGT0edLEcZS3LcFEeew7doeZq1t8JKBHe1PxyuW4rGHEG1lDlBb1cj8x1fFBKPbSzYZiY/lpnnXzLgYJfjs2ctxoChiqdK+5PH6E9giXaYAMxTuiI17rBCO7yOZur4bBwPfMKyFlo/dTt/DoNFM1mKvPqe6g7VjD794BrNzQ/o4K9VEACN/CQfwaKh1e6uIMxqqkjobaSczw8UWevQqa3LATXBt+0gBAMCjVfw1XxM4/ZraHMrJ+qyY082t/KrXscrufL+JbENq68ad/Pj+qCb8t5r6C8=~1",
        "bm_sv": "765F8D6CD3BFDD3456484A26533C20C7~YAAQEqwwF7eD+XmEAQAAKr9zjhH5e2WzMLA823HiaPPza2nVOLsbR0xAa5M/KseB73YFNdMG9jyRWFReNEFPD7S4FYgFxz2Wke+Z1Z2mXiFyzOyAeJPpmqt3ulWMi722Ckbi15GXEm3RVaIwsZ1V18ts49AfDoEpDgsuM94vbb37tfIe/YgeRQQhtYENvOP08VQR7Bcm8EEha8kTukVhtYz6iAgEFTZ7AF4cKWaH6zW1VPmzMD93Y0JBws18yQpGvl4=~1",
        "ak_bmsc": "BFCEB6939AEA451C0969984C64923939~000000000000000000000000000000~YAAQEqwwFwOE+XmEAQAAhhl1jhHeE6JVj8puP7cAdxKzRdLN06ZaHRuCblEIVhCR2j+dbNMeqck1O71GNVSX79SBMkc7g4iUTW2mBftfUDcglkDJmHmoNCA8SAstgmDm8iSP/6j+JdgR/jb3XaFGAL36ukMsa5Cs8SDlWV6yUp9iySQPaDaGMKpAqFuiyq5zfqH4zMbNyDs5bRS1g9+mOB8X5EYB8c+x0JQ0/nbkOeZColKBn9sD+AX0v9BIAdC+/nOGP3apkIdZOZZXH3Lb/mNd3PNltKg0hUXO5upYlNZixh6VlLQRtAJBpj9xXBKalssQyUoQZGbjXc2MKeifU359h6ISSMG9LzIVCoZKULP0WjxbQ2W22Cx6fdee+bIjLc1fkz+AZ39KC7xcFZV4oPgS6KBTBkSKdOv9SI6RW3JsgSE1l93j",
        "adblocked": "true",
        "com.wm.reflector": "\"reflectorid:0000000000000000000000@lastupd:1668837615000@firstcreate:1668759547743\"",
        "xptwj": "rq:2f0c81dabca7e41af4a9:ReWuChXZ6IUO2Rbh/vx0rLi5t8iaPzWYTnedGlu9TeEkanBGWTX3IldqTA0DYGXxpdYCWBBP5E9Y2y6S8B+hX0z3gMeo7HE16f5eLFsP3s1wLEs2qkg9+l2Iui6ErCt5ddzEZPP/WfAkB4Ezjg==",
        "akavpau_p2": "1668838215~id=697cb8f019e5812cb706926bda052dfe",
        "xptwg": "3856602461:1DC7671C79E3AD0:4CA3CDA:97CC9CC5:A36A2E2F:E86E578D:",
        "TS012768cf": "01db7b26b5c803720ff10676ee81c40a646b4751c8442a4d16824183de77485b6923b67898d3e63f1d9c013fbff989627c913be786",
        "TS01a90220": "01db7b26b5c803720ff10676ee81c40a646b4751c8442a4d16824183de77485b6923b67898d3e63f1d9c013fbff989627c913be786",
        "TS2a5e0c5c027": "084cb511abab2000f9253fdb5f89d3fea7f627bf373cc6baca55fc8b4cea145e14e1e890f4fa7f860856e8cf7811300020c45eab116805f5650415bf1b88334bc644ba08db1b65165f75ecb890ed78d6cea595f8f9b2372364d9006aad058425"
    }

    def start_requests(self):
        for i in range(1, 26):
            request = Request(
                url=self.url.format(i),
                # url=self.url,
                method="GET",
                dont_filter=True,
                cookies=self.cookies,
                headers=self.headers,
                callback=self.parse
            )
            yield request

    def parse(self, response):
        # inspect_response(response, self)
        raw_data = response.body
        data = json.loads(raw_data)

        for i in range(len(data['data']['search']['searchResult']['itemStacks'][0]['itemsV2'])):
            try:
                item = {
                    'Name':  data['data']['search']['searchResult']['itemStacks'][0]['itemsV2'][i]['name'],
                    'Price': data['data']['search']['searchResult']['itemStacks'][0]['itemsV2'][i]['priceInfo']['currentPrice']['price'],
                    'Availability': data['data']['search']['searchResult']['itemStacks'][0]['itemsV2'][i]['availabilityStatusV2']['value'],
                    'Link URL': data['data']['search']['searchResult']['itemStacks'][0]['itemsV2'][i]['canonicalUrl'],
                    'Average Rating': data['data']['search']['searchResult']['itemStacks'][0]['itemsV2'][i]['averageRating'],
                    'Number of Reviews': data['data']['search']['searchResult']['itemStacks'][0]['itemsV2'][i]['numberOfReviews'],
                }
                yield item
            except Exception:
                item = {
                    'Name':  data['data']['search']['searchResult']['itemStacks'][0]['itemsV2'][i]['name'],
                    'Availability': 'Out Of Stock',
                }
                yield item
