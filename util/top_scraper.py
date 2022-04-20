import httpx
from colorama import Fore as F, init; init()
from util.write import write

def top_scraper(amount, query = ""):
    servers = httpx.get(
        f"https://top.gg/api/client/entities/search?platform=discord&entityType=server&amount={amount}&nsfwLevel=1&newSortingOrder=TOP_VOTED&sort=top&query={query}"
    ).json()["results"]

    for server in servers:
        id = server["id"]
        server = httpx.get(f"https://top.gg/servers/{id}/join", follow_redirects = True)
        print(f"{F.LIGHTGREEN_EX}[+] {F.LIGHTMAGENTA_EX}{str(server.url)}{F.RESET}")
        write(str(server.url) + "\n")