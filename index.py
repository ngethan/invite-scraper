import httpx, ctypes, os, sys, time, urllib3
from colorama import Fore as F, init
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from yaml import safe_load

init()
ctypes.windll.kernel32.SetConsoleTitleW(f'aurora invite scrapper v0.1')

invites_exists = os.path.isfile('invites.txt')
config_exist = os.path.isfile('config.yml')
if not invites_exists:
    file = open('invites.txt', 'x')
    file.close()

try:
    config = safe_load(open('config.yml', 'r', encoding='utf-8', errors='ignore'))
    server_amount = int(config['server_amount'])
    website = str(config['website'])
    use_search_query = bool(config['use_search_query'])
    search_queries = list(config['search_queries'])
except Exception as e:
    print(f'{F.RED}Error: {e}')
    time.sleep(5)
    sys.exit()

def banner():
    print(F.GREEN + """
 █████╗ ██╗   ██╗██████╗  ██████╗ ██████╗  █████╗ 
██╔══██╗██║   ██║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗
███████║██║   ██║██████╔╝██║   ██║██████╔╝███████║
██╔══██║██║   ██║██╔══██╗██║   ██║██╔══██╗██╔══██║
██║  ██║╚██████╔╝██║  ██║╚██████╔╝██║  ██║██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝""" + F.LIGHTMAGENTA_EX + """\n
            Discord Invite Scrapper""" + F.BLUE + """
         https://discord.gg4rHg2pyHjF""" + "\n" + F.RESET)

def topgg_scraper(amount, query = ""):
    servers = httpx.get(
        f"https://top.gg/api/client/entities/search?platform=discord&entityType=server&amount={amount}&nsfwLevel=1&newSortingOrder=TOP_VOTED&sort=top&query={query}"
    ).json()["results"]

    for server in servers:
        id = server["id"]
        server = httpx.get(f"https://top.gg/servers/{id}/join", follow_redirects=True)
        print('\033[01m' + F.LIGHTGREEN_EX + '[✓] ' + F.LIGHTMAGENTA_EX + str(server.url) + F.RESET)
        write(str(server.url) + "\n")

def write(str):
    with open("invites.txt", "a") as f:
        f.write(str)

banner()
final_servers = []
print("Scraping...")
if website == "top":
    if use_search_query:
        for i in range(len(search_queries)):
            topgg_scraper(int(server_amount), search_queries[i])
            print("Finished scraping for search query " + "\"" + search_queries[i] + "\"")
    else:
        topgg_scraper(int(server_amount), "")
elif website == "discordtop":
    pass
elif website == "discordhome":
    pass
else:
    print("Error: Invalid website")
    time.sleep(5)
    sys.exit()

print(F.GREEN + "Finished" + F.RESET)