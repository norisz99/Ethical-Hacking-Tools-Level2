# 🚀 Advanced Multi-Threaded Port Scanner

## 📌 Áttekintés (Overview)
Ez a Python alapú eszköz a hálózati felderítés (Reconnaissance) egyik legfontosabb fázisát, a portszkennelést gyorsítja fel drasztikusan. A hagyományos, szekvenciális szkennerekkel ellentétben ez a program **Többszálú (Multi-threading)** technológiát használ, így egyszerre több száz portot képes vizsgálni párhuzamosan.

## 🛠️ Funkciók
* **⚡ Nagy sebesség:** 1024 port ellenőrzése másodpercek alatt (vs. percek).
* **🧵 Multi-threading:** `threading` és `Queue` könyvtárak használata a párhuzamos munkavégzéshez.
* **🎯 DNS Feloldás:** Domain nevek (pl. google.com) automatikus IP-re fordítása.
* **📊 Rendezett kimenet:** Csak a nyitott portokat listázza, növekvő sorrendben.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Könyvtárak:** `socket`, `threading`, `queue`, `time`
* **Módszer:** TCP Connect Scan (Teljes kézfogás).
* **Szálkezelés:** Producer-Consumer minta (Queue) használata a szálak szinkronizálására.

## 🚀 Használat

**Futtatás:**
```bash
python fast_scanner.py