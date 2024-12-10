#!/usr/bin/env python3

import sys
import socket
import threading
import time

#Contador de puertos
open_ports = []

# Función para escanear un puerto en particular
def scan_port(ip, port):
    try:
        # Crear un socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            # Intentar conectar al puerto
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)
                print(f"[+] Puerto {port} abierto en {ip}")
    except Exception as e:
        pass

# Función para escanear un rango de puertos
def port_scanner(ip, start_port, end_port):
    print(f"Usando IP: {target_ip}, Rango de puertos: {start_port}-{end_port}")
    threads = []
    start_time = time.time()

    for port in range(start_port, end_port + 1):
        # Crear un hilo para cada puerto
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    # Esperar a que todos los hilos terminen
    for t in threads:
        t.join()

    print("\nEscaneo completo.")
    print(f"Total de puertos abiertos: {len(open_ports)}")

    elapsed_time = time.time() - start_time
    print(f"Tiempo total: {elapsed_time:.2f} segundos")

# Main
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: ps <target_ip> <start_port> <end_port>")
        sys.exit(1)

    target_ip = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    port_scanner(target_ip, start_port, end_port)
