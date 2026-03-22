import requests
from bs4 import BeautifulSoup
import re
import time

TARGETS = ["site:.gov.za", "site:.ac.za", "site:mtn.co.za", "site:vodacom.co.za"]
HEADERS = {"User-Agent": "Mozilla/5.0 Chrome/121.0.0.0"}

def hunt():
    print("\033[1;36m[ LegendsHub™ ] Scouring the web...\033[0m")
    gold = []
    for t in TARGETS:
        try:
            r = requests.get(f"https://www.google.com/search?q={t}+-inurl:www", headers=HEADERS, timeout=10)
            soup = BeautifulSoup(r.text, 'html.parser')
            for a in soup.find_all('a', href=True):
                match = re.search(r'url\?q=(https?://[^&]+)', a['href'])
                if match:
                    host = match.group(1).split('/')[2]
                    try:
                        check = requests.head(f"https://{host}", timeout=3, headers=HEADERS)
                        if check.status_code in [200, 301, 302]:
                            print(f"\033[1;32m[+] CAPTURED: {host}\033[0m")
                            gold.append(host)
                    except:
                        continue
            time.sleep(2)
        except:
            continue
    
    with open("Legends_Gold.txt", "w") as f:
        for bug in list(set(gold)):
            f.write(f"HOST: {bug} | STATUS: VERIFIED\n")
    print("\033[1;32m[✔] Hunt Complete. Results saved.\033[0m")

if __name__ == "__main__":
    hunt()

