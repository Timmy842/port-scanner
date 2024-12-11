#!/usr/bin/env python3

import sys
import time

from helpers.helper import show_help
from helpers.scanner import port_scanner
from helpers.saver import save_results

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

    start_time = time.time()
    open_ports = port_scanner(target_ip, start_port, end_port)
    elapsed_time = time.time() - start_time

    print("\nEscaneo completo.")
    print(f"Total de puertos abiertos: {len(open_ports)}")
    print(f"Tiempo total: {elapsed_time:.2f} segundos")

    if file_type:
        save_results(target_ip, start_port, end_port, open_ports, file_type)

