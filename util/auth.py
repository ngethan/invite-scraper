import httpx, subprocess

name = "aurora_invite_scraper"
owner_id = "YMaG4tFeED"
session_id = httpx.get(f"https://keyauth.win/api/1.1/?type=init&ver=1.0&name={name}&ownerid={owner_id}").json()['sessionid']

def get_hwid():
    cmd = 'wmic csproduct get uuid'
    hwid = str(subprocess.check_output(cmd))
    pos1 = hwid.find("\\n")+2
    hwid = hwid[pos1:-15]
    return hwid

def login(auth_key):
    success = httpx.get(f"https://keyauth.win/api/1.1/?type=license&key={auth_key}&hwid={get_hwid()}&sessionid={session_id}&name={name}&ownerid={owner_id}").json()['success']

    if success: return True
    else: return False