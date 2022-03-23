import requests, httpx, ctypes
from bs4 import BeautifulSoup
from colorama import Fore as F, init
from collections import OrderedDict

init()
ctypes.windll.kernel32.SetConsoleTitleW(f'ykcehc v0.1 Discord Invite Scrapper')

def banner():
    print(
        F.LIGHTRED_EX
        + """
    ██████╗ ███████╗██████╗  █████╗ ██████╗  ██████╗███████╗
    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
    ██████╔╝█████╗  ██████╔╝███████║██████╔╝██║     ███████╗
    ██╔══██╗██╔══╝  ██╔═══╝ ██╔══██║██╔══██╗██║     ╚════██║
    ██║  ██║███████╗██║     ██║  ██║██║  ██║╚██████╗███████║
    ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝
       
                Discord Invite Scrapper
              https://discord.gg4rHg2pyHjF
"""     
        + F.RESET)

banner()

servers = []; counter = 1

server_amount = int(input("How many servers would you like to scrape? "))
print(f"Scraping... This will take about {server_amount} seconds")

while len(servers) < server_amount:
    url = f"https://top.gg/servers/list/new?page={counter}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = list(OrderedDict.fromkeys(soup.find_all("a", class_ = "chakra-link")))

    for a in results:
        if a["href"].endswith("/join"):
            server = str(httpx.get(f"https://top.gg{a['href']}", follow_redirects = True).url)
            servers.append(server)
    
    counter += 1

with open("servers.txt", "w") as f:
        f.write("\n".join(servers[0:server_amount]))

print("Done!")