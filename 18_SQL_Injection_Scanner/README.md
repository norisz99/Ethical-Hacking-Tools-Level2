# 💉 Simple SQL Injection Scanner

## 📌 Áttekintés (Overview)
Ez az eszköz automatizáltan vizsgálja a webes URL-eket SQL Injection (SQLi) sebezhetőségek után kutatva. A program különböző "támadó" karakterláncokat (payloadokat) fűz a megadott URL paramétereihez, és figyeli a szerver válaszában megjelenő, adatbázis-hibára utaló üzeneteket (Error-Based Detection).

## 🛠️ Funkciók
* **Payload Injection:** Automatikus tesztelés gyakori SQLi karakterekkel (`'`, `"`, `OR 1=1`).
* **Error Detection:** Képes felismerni a leggyakoribb adatbázis-motorok (MySQL, PostgreSQL, Microsoft SQL Server) hibaüzeneteit a HTML válaszban.
* **Intelligens Elemzés:** Jelzi, ha az URL nem tartalmaz tesztelhető paramétert.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Könyvtár:** `requests`
* **Módszer:** GET kérések manipulálása és String Matching a válaszban.

## 🚀 Használat

**Futtatás:**
```bash
python sql_scanner.py
Példa Bemenet: http://testphp.vulnweb.com/artists.php?artist=1