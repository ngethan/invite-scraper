import requests, httpx, math
from bs4 import BeautifulSoup
from colorama import Fore as F, init; init()
from util.write import write

def dhome_scraper(amount, query=""):
    counter = 0
    for i in range(math.ceil(amount/24)):
        url = f"https://discordhome.com/?order=voted&page={i}" if not query else f"https://discordhome.com/servers/search?q={query}&o=top-voted&page={i}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all("a", class_ = "join")
        
        for a in results:
            if counter == amount: break
            server = httpx.get(f"https://discordhome.com{a['href']}", follow_redirects = True)
            print(f"{F.LIGHTGREEN_EX}[+] {F.LIGHTMAGENTA_EX}{str(server.url)}{F.RESET}")
            write(str(server.url) + "\n")
            counter += 1