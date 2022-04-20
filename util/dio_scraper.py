import httpx, re, math
from colorama import Fore as F, init; init()
from util.write import write

def dio_scraper(amount, query):
    counter = 0
    for i in range(math.ceil(amount/15)):
        r = httpx.get(f"https://discord.io/servers?q={query}&filter=&page={i}") 
        link = re.findall(r'fab fa-discord"></i>(.*?)</li>',str(r.text))

        for li in link:
            try:
                if counter == amount: break
                r = httpx.get(f'https://{li}')
                server = f"""{F.LIGHTGREEN_EX}[+] {F.LIGHTMAGENTA_EX}{re.search(r'window.location="(.*?)"',str(r.text)).group(1)}{F.RESET}"""
                print(server)
                write(re.search(r'window.location="(.*?)"',str(r.text)).group(1) + "\n")
                counter += 1
            except:
                pass