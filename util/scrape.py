import sys, time
from util.top_scraper import top_scraper

def scrape(website, server_amount, use_search_query, search_queries):
    if website == "top":
        if use_search_query:
            for i in range(len(search_queries)):
                top_scraper(int(server_amount), search_queries[i])
                print("Finished scraping for search query " + "\"" + search_queries[i] + "\"")
        else:
            top_scraper(int(server_amount), "")
    elif website == "discordtop":
        pass
    elif website == "discordhome":
        pass
    else:
        print("Error: Invalid website")
        time.sleep(5)
        sys.exit()