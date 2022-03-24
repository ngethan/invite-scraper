import ctypes, os, sys, time, urllib3
from colorama import Fore as F, init; init()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from yaml import safe_load
ctypes.windll.kernel32.SetConsoleTitleW(f'aurora invite scrapper v0.1')

# invite file check & config initialization
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

# importing methods
from util.scrape import scrape


print(F.GREEN + """
 █████╗ ██╗   ██╗██████╗  ██████╗ ██████╗  █████╗ 
██╔══██╗██║   ██║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗
███████║██║   ██║██████╔╝██║   ██║██████╔╝███████║
██╔══██║██║   ██║██╔══██╗██║   ██║██╔══██╗██╔══██║
██║  ██║╚██████╔╝██║  ██║╚██████╔╝██║  ██║██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝""" + F.LIGHTMAGENTA_EX + """\n
            Discord Invite Scrapper""" + F.BLUE + """
         https://discord.gg4rHg2pyHjF""" + "\n" + F.RESET)
final_servers = []
print("Scraping...")
scrape(website, server_amount, use_search_query, search_queries)
print(F.GREEN + "Finished" + F.RESET)