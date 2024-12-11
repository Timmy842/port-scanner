import socket
import threading

# Contador global de puertos abiertos
open_ports = []

# Función para escanear un puerto en particular
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)
                print(f"[+] Puerto {port} abierto en {ip}")
    except Exception as e:
        pass

# Función para escanear un rango de puertos
def port_scanner(ip, start_port, end_port):
    print(f"Escaneando {ip} desde el puerto {start_port} hasta {end_port}...\n")
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return open_ports
