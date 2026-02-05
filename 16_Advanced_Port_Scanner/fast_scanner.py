import socket
import threading
from queue import Queue
import time

# Színek a profi kinézethez
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# A szálak (párhuzamos munkások) száma
# Ha túl magas (pl. 500), a routered letilthat, de 50-100 biztonságos.
THREAD_COUNT = 100

# Ide gyűjtjük a feladatokat (portokat)
queue = Queue()
open_ports = []

def port_scan(target, port):
    """Ez a függvény végez egyetlen kopogtatást."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Ha 1 mp alatt nem válaszol, továbblépünk
        
        # Kapcsolódási kísérlet
        result = s.connect_ex((target, port))
        
        if result == 0:
            return True
        s.close()
    except:
        pass
    return False

def worker(target):
    """Ez a munkás (Thread) addig dolgozik, amíg van feladat a sorban."""
    while not queue.empty():
        port = queue.get()
        if port_scan(target, port):
            print(f"{GREEN}[+] Port {port} NYITVA{RESET}")
            open_ports.append(port)
        queue.task_done()

def run_scanner(target, start_port=1, end_port=1024):
    print(f"\n--- 🚀 ADVANCED MULTI-THREADED SCANNER ---")
    print(f"[*] Célpont: {target}")
    print(f"[*] Portok: {start_port}-{end_port}")
    print(f"[*] Szálak száma: {THREAD_COUNT}")
    print("------------------------------------------")
    
    start_time = time.time()

    # 1. Feltöltjük a feladatlistát (Queue) a portokkal
    for port in range(start_port, end_port + 1):
        queue.put(port)

    # 2. Elindítjuk a munkásokat (Threads)
    thread_list = []
    for _ in range(THREAD_COUNT):
        thread = threading.Thread(target=worker, args=(target,))
        thread_list.append(thread)
        thread.start()

    # 3. Megvárjuk, amíg mindenki végez
    queue.join()
    
    duration = time.time() - start_time
    print("------------------------------------------")
    print(f"✅ Kész! Vizsgálati idő: {duration:.2f} másodperc")
    
    if open_ports:
        print(f"\n🔓 Nyitott portok listája: {sorted(open_ports)}")
    else:
        print(f"\n🔒 Nem találtunk nyitott portot ebben a tartományban.")

if __name__ == "__main__":
    target_input = input("Add meg a célpont IP címét (pl. 192.168.0.1 vagy google.hu): ")
    
    # Ha domaint ad meg, átváltjuk IP-re
    try:
        target_ip = socket.gethostbyname(target_input)
        print(f"[*] IP cím feloldva: {target_ip}")
        
        # Futtatás (Alapból az első 1024 portot nézzük, ezek a legfontosabbak)
        run_scanner(target_ip, 1, 1024)
        
    except socket.gaierror:
        print(f"{RED}❌ HIBA: Érvénytelen cím!{RESET}")