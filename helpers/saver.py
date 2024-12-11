import json

# Función para guardar resultados en un archivo
def save_results(ip, start_port, end_port, open_ports, file_type):
    if file_type == "-ft":
        file_name = "scan_results.txt"
        with open(file_name, "w") as f:
            f.write(f"Resultados del escaneo de {ip} (puertos {start_port} - {end_port}):\n")
            for port in open_ports:
                f.write(f"Puerto {port} abierto\n")
        print(f"\nResultados guardados en {file_name}")
    elif file_type == "-fj":
        file_name = "scan_results.json"
        results = {"ip": ip, "open_ports": open_ports}
        with open(file_name, "w") as f:
            json.dump(results, f, indent=4)
        print(f"\nResultados guardados en {file_name}")
    else:
        print("\nError: Tipo de archivo no reconocido. Usa -ft o -fj.")
