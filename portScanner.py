import socket
import threading

# Función para escanear un puerto en particular
def scan_port(ip, port):
    try:
        # Crear un socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            # Intentar conectar al puerto
            if s.connect_ex((ip, port)) == 0:
                print(f"[+] Puerto {port} abierto en {ip}")
    except Exception as e:
        pass

# Función para escanear un rango de puertos
def port_scanner(ip, start_port, end_port):
    print(f"Escaneando {ip} desde el puerto {start_port} hasta {end_port}...")
    threads = []

    for port in range(start_port, end_port + 1):
        # Crear un hilo para cada puerto
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    # Esperar a que todos los hilos terminen
    for t in threads:
        t.join()

    print("Escaneo completo.")

# Main
if __name__ == "__main__":
    target_ip = input("Introduce la IP objetivo: ")
    start_port = int(input("Introduce el puerto inicial: "))
    end_port = int(input("Introduce el puerto final: "))
    port_scanner(target_ip, start_port, end_port)
