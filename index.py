import httpx, ctypes, math
from colorama import Fore as F, init

init()
ctypes.windll.kernel32.SetConsoleTitleW(f'ykcehc v0.1 Discord Invite Scrapper')

def banner():
    print(F.LIGHTBLUE_EX + """
██████╗ ███████╗██████╗  █████╗ ██████╗  ██████╗███████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝█████╗  ██████╔╝███████║██████╔╝██║     ███████╗
██╔══██╗██╔══╝  ██╔═══╝ ██╔══██║██╔══██╗██║     ╚════██║
██║  ██║███████╗██║     ██║  ██║██║  ██║╚██████╗███████║
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝""" + F.LIGHTYELLOW_EX + """\n
            Discord Invite Scrapper
         https://discord.gg4rHg2pyHjF""" + F.RESET)

def topgg_scraper(amount):
    servers = httpx.get(
        f"https://top.gg/api/client/entities/search?platform=discord&entityType=server&amount={amount}&nsfwLevel=1&sort=top"
    ).json()["results"]

    for server in servers:
        id = server["id"]
        server = httpx.get(f"https://top.gg/servers/{id}/join", follow_redirects=True)
        print('\033[01m' + F.LIGHTGREEN_EX + '[✓] ' + F.LIGHTYELLOW_EX + str(server.url) + F.RESET)
        write(str(server.url) + "\n")

def write(str):
    with open("servers.txt", "a") as f:
        f.write(str)

print("✓")
banner()

final_servers = []
server_amount = int(input(F.LIGHTBLUE_EX + "How many servers would you like to scrape? " + F.RESET))
print(f"Scraping...")
topgg_scraper(int(server_amount))
print("Done!")