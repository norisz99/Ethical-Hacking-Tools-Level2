# 🔨 Universal Brute Force Login Cracker (v2.0)

## 📌 Áttekintés (Overview)
Ez a továbbfejlesztett eszköz egy univerzális jelszótörő alkalmazás, amely bármely szabványos HTTP POST alapú bejelentkezési felületen használható. A program dinamikusan konfigurálható, így a felhasználó szabadon megadhatja a célpont mezőneveit és a sikerességet jelző kulcsszavakat. Támogatja a külső szótárfájlok (.txt) használatát.

## 🛠️ Funkciók
* **Interactive CLI:** A futtatáskor paraméterezhető célpont, felhasználónév és mezőnevek.
* **Custom Field Names:** Bármilyen űrlaphoz igazítható (pl. `username` vs `email`, `pwd` vs `password`).
* **Wordlist Support:** Külső jelszólisták (.txt) beolvasása memóriakímélő módon.
* **Smart Detection:** A sikeres belépést a felhasználó által definiált kulcsszó (pl. "Welcome", "Logout") alapján azonosítja.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Könyvtár:** `requests`, `sys`, `os`
* **Bemenet:** Standard Input & Text file I/O.

## 🚀 Használat

**Futtatás:**
```bash
python login_cracker_v2.py