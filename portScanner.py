#!/usr/bin/env python3

import sys
import socket
import threading
import time
import json

from helper import show_help

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
def port_scanner(ip, start_port, end_port, file_type = None):
    print(f"Usando IP: {target_ip}, Rango de puertos: {start_port} - {end_port}\n")
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

    if file_type:
        save_results(ip, start_port, end_port, file_type)

# Guardar resultados en un archivo
def save_results(ip, start_port, end_port, file_type):
    # Guardar en archivo de texto
    if file_type == "-ft":
        file_name = "scan_results.txt"
        with open(file_name, "w") as f:
            f.write(f"Resultados del escaneo de {ip} (puertos {start_port}-{end_port}):\n")
            for port in open_ports:
                f.write(f"Puerto {port} abierto\n")
        print(f"\nResultados guardados en {file_name}")

    # Guardar en archivo JSON
    elif file_type == "-fj":
        file_name = "scan_results.json"
        results = {"ip": ip, "open_ports": open_ports}
        with open(file_name, "w") as f:
            json.dump(results, f, indent=4)
        print(f"\nResultados guardados en {file_name}")

    else:
        print("\nError: Tipo de archivo no reconocido. Usa -ft o -fj.")

# Main
if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help"):
        show_help()
        sys.exit(0)
    
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        print("Uso: portscanner <IP> <puerto_inicial> <puerto_final> [-ft|-fj]")
        sys.exit(1)

    target_ip = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    file_type = sys.argv[4] if len(sys.argv) == 5 else None

    if file_type and file_type not in ("-ft", "-fj"):
        print("Error: Opción inválida. Usa -ft para texto o -fj para JSON.")
        sys.exit(1)

    if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
        print("Error: Los puertos deben estar en el rango 1-65535.")
        sys.exit(1)

    if start_port > end_port:
        print("Error: El puerto inicial no puede ser mayor que el puerto final.")
        sys.exit(1)


    port_scanner(target_ip, start_port, end_port, file_type)
