import sys, time
from util.top_scraper import top_scraper
from util.dhome_scraper import dhome_scraper
from util.dst_scraper import dst_scraper
from util.dio_scraper import dio_scraper

def scrape(website, amount, use_search_query, search_queries):
    if website == "top":
        if use_search_query:
            for i in range(len(search_queries)):
                top_scraper(int(amount), search_queries[i])
                print("Finished scraping for search query " + "\"" + search_queries[i] + "\"")
        else:
            top_scraper(int(amount))
    elif website == "discordhome":
        if use_search_query:
            for i in range(len(search_queries)):
                dhome_scraper(int(amount), search_queries[i])
                print("Finished scraping for search query " + "\"" + search_queries[i] + "\"")
        else:
            dhome_scraper(int(amount))
    elif website == "discordst":
        if use_search_query:
            for i in range(len(search_queries)):
                dst_scraper(int(amount), search_queries[i])
                print("Finished scraping for search query " + "\"" + search_queries[i] + "\"")
        else:
            dst_scraper(int(amount))
    elif website == "discordio":
        if use_search_query:
            for i in range(len(search_queries)):
                dio_scraper(int(amount), search_queries[i])
                print("Finished scraping for search query " + "\"" + search_queries[i] + "\"")
    else:
        print(f'{F.RED}Error: Invalid website')
        time.sleep(5)
        sys.exit()