# Walmart-Scraping-SearchItems-API-scraping
- Web scraping via hidden API in walmart.com
- Extracting search items into a list.
- Scraping framework : Scrapy
- Scraping through API, extracting data from JSON

# Result
- Please see the generated scraped data in [result](https://github.com/allifizzuddin89/Walmart-Scraping-SearchItems-API-scraping/blob/main/Walmart_SearchItems_Scraping_API/Walmart_SearchItems_Scraping_API/spiders/Walmart_coffee_machine.csv)

## Requirement : 
- Scrapy 2.7.1
- Python 3.7 or above
- Any working environment to install the required packages such as conda or pyenv.

## Run
- The working directory is Walmart-Scraping-SearchItems-API-scraping/Walmart_SearchItems_Scraping_API/Walmart_SearchItems_Scraping_API/spiders/
- Activate the installed working environment
- Run the main.py in the working directory.
- Run <scrapy runspider main.py> in the terminal in the working directory
  OR simply run <scrapy crawl main.py>
- Add '-O walmart_coffee.csv' in terminal to produce the csv file e.g. 'scrapy runspider main.py -O walmart_coffee.csv'

### Install environment
- Refer [CONDA Environment Installation](https://docs.anaconda.com/anaconda/install/)
 
### HOW-TO
- Clone the repository
```bash  
  git clone https://github.com/allifizzuddin89/Walmart-Scraping-SearchItems-API-scraping.git 
```
- Create working environment (skip if already have any working environment)
```bash
  conda create --name scraping_env -c conda-forge python=3.9.13 scrapy=2.7.1
```
- Activate the working environment
```bash
  conda activate scraping_env
```
 - Run the spider
 ```bash
    scrapy runspider Walmart-Scraping-SearchItems-API-scraping.Walmart_SearchItems_Scraping_API.Walmart_SearchItems_Scraping_API.spiders.main.py -O walmart_coffee.csv
 ```

## Troubleshoot
- Error might happened due to the cookies already expired or request being rejected by the server or the url simply has been changed by the administrator.
- Solution: 
  1. Refresh the cookies (if any) OR
  2. Using proxy (refer main.py) OR
  3. Replace existing url with the new url
  
## DISCLAIMER
- This work only meant for educational, research and proof of work purpose only. 
- I will not responsible for any illegal activities.
- Every action is on your own responsibilities.
