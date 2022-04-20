import requests, httpx, math
from bs4 import BeautifulSoup
from colorama import Fore as F, init; init()
from util.write import write

def dst_scraper(amount, query=""):
    counter = 0
    for i in range(math.ceil(amount/15)):
        url = f"https://discord.st/?page={i}" if not query else f"https://discord.st/?page={i}&q={query}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all("a", text = "Join")

        for a in results:
            if counter == amount: break
            server = httpx.get(f"https://discord.st{a['href']}", follow_redirects = True)
            print(f"{F.LIGHTGREEN_EX}[+] {F.LIGHTMAGENTA_EX}{str(server.url)}{F.RESET}")
            write(str(server.url) + "\n")
            counter += 1