# 🦈 Network Packet Sniffer (Scapy)

## 📌 Áttekintés (Overview)
Ez a projekt egy Python alapú hálózati forgalom-elemző eszköz (Packet Sniffer), amely a **Scapy** könyvtárat használja. A program képes valós időben "lehallgatni" a hálózati interfészt, és megjeleníteni az áthaladó adatcsomagokat.

Különlegessége, hogy képes különbséget tenni a protokollok között, és demonstrálja a **titkosítatlan (HTTP)** forgalom veszélyeit azzal, hogy elfogja és megjeleníti a nyers adatforgalmat (pl. HTML kód, képek metaadatai, szöveges tartalom).

## 🛠️ Funkciók
* **🔍 Valós idejű megfigyelés:** TCP, UDP és ICMP csomagok azonnali detektálása.
* **🎯 Intelligens Szűrés (Smart Filtering):** Beépített szűrő, amely képes leválasztani a zajt (pl. NDI videófolyamok, Windows Update) és csak a célzott webes forgalomra (TCP Port 80) fókuszálni.
* **🔓 Payload Extraction:** A HTTP csomagok "Raw" (nyers) adattartalmának dekódolása és megjelenítése.
* **🎨 Visual Interface:** Színkódolt kimenet a könnyebb átláthatóságért (Zöld=TCP, Sárga=UDP, Piros=ICMP, Cián=Adat).

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Könyvtár:** `scapy` (Advanced interactive packet manipulation program).
* **Működési elv:** A hálózati kártyát "Promiscuous Mode"-ba kapcsolja, így minden csomagot lát, nem csak a gépnek címzetteket.

## 🚀 Telepítés & Használat

1. **Függőségek telepítése:**
   ```bash
   pip install scapy
## ⚠️ Jogi Nyilatkozat (Disclaimer)
Ez az eszköz kizárólag **oktatási és saját hálózat-diagnosztikai célokra** készült. Mások hálózati forgalmának engedély nélküli megfigyelése vagy rögzítése törvénybe ütköző cselekmény lehet. Használd felelősséggel!