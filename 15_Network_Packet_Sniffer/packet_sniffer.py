import sys
from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

# Színek a terminálhoz (hogy profin nézzen ki)
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def packet_callback(packet):
    """
    Ez a függvény hívódik meg minden egyes elkapott csomagnál.
    """
    
    # Csak az IP csomagokkal foglalkozunk
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "EGYÉB"
        color = RESET
        
        # Protokoll típusának meghatározása és színezése
        if packet.haslayer(TCP):
            protocol = "TCP"
            color = GREEN
        elif packet.haslayer(UDP):
            protocol = "UDP"
            color = YELLOW
        elif packet.haslayer(ICMP):
            protocol = "ICMP"
            color = RED
            
        # Kiírjuk az alapadatokat: [PROTOKOLL] Feladó -> Címzett
        print(f"{color}[{protocol}]{RESET} {src_ip} -> {dst_ip}")
        
        # --- LEVEL 2 EXTRA: Adattartalom (Payload) vizsgálata ---
        # Ha a csomag "Raw" (nyers) adatot tartalmaz, megpróbáljuk kiolvasni.
        # Ez lehet pl. egy HTTP kérés részlete, vagy egy chat üzenet.
        if packet.haslayer("Raw"):
            try:
                # Megpróbáljuk szöveggé alakítani (utf-8)
                load = packet["Raw"].load.decode('utf-8', 'ignore')
                
                # Ha nem üres, kiírjuk (de csak az első 100 karaktert, hogy ne szemetelje tele a képernyőt)
                if load.strip():
                    print(f"{CYAN}    └── 📦 ADAT: {load[:100].replace('\n', ' ')}...{RESET}")
            except:
                pass # Ha nem szöveges adat (pl. kép binary), akkor csendben maradunk

def start_sniffer():
    print(f"\n--- 🦈 NETWORK PACKET SNIFFER (HTTP ONLY) ---")
    print(f"[*] Figyelés indítása... {YELLOW}(Nyomj Ctrl+C-t a leállításhoz){RESET}")
    print(f"[*] SZŰRŐ AKTÍV: Csak a TCP 80-as port (Titkosítatlan Web) forgalmát nézzük.")
    
    try:
        # A filter="tcp port 80" a kulcs!
        # Ez kuka minden mást (HTTPS, NDI, Windows Update), csak a tiszta szöveg marad.
        sniff(filter="tcp port 80", store=False, prn=packet_callback)
        
    except KeyboardInterrupt:
        print("\n[*] Leállítás...")
    except PermissionError:
        print(f"\n{RED}❌ HIBA: Futtasd Rendszergazdaként!{RESET}")
    except Exception as e:
        print(f"\n{RED}❌ Hiba: {e}{RESET}")

if __name__ == "__main__":
    start_sniffer()