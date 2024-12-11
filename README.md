
# PortScanner

PortScanner es una herramienta sencilla para escanear puertos abiertos en un rango específico utilizando Python. Permite identificar servicios abiertos en una dirección IP objetivo y guardar los resultados en diferentes formatos.

## Características

- Escaneo rápido y concurrente utilizando hilos.
- Soporte para guardar resultados en:
  - Archivo de texto (`-ft`)
  - Archivo JSON (`-fj`)
- Validación de argumentos y rango de puertos.
- Uso intuitivo desde la terminal.

## Requisitos

- Python 3.x
- Sistema operativo Linux (probado en Kali Linux, Ubuntu, y Rocky Linux)

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/portscanner.git
   cd portscanner
   ```

## Uso

### Ejemplo de comando
```bash
portscanner <IP> <puerto_inicial> <puerto_final> [-ft|-fj]
```

### Opciones

| Parámetro | Descripción                                      |
|-----------|--------------------------------------------------|
| `<IP>`    | Dirección IP objetivo (obligatorio).            |
| `<puerto_inicial>` | Primer puerto a escanear (obligatorio).  |
| `<puerto_final>`   | Último puerto a escanear (obligatorio).  |
| `-ft`     | Guarda los resultados en un archivo de texto.    |
| `-fj`     | Guarda los resultados en un archivo JSON.        |

### Ejemplos
1. Escaneo simple sin guardar resultados:
   ```bash
   portscanner 192.168.0.39 1 100
   ```

2. Guardar resultados en texto:
   ```bash
   portscanner 192.168.0.39 1 100 -ft
   ```

3. Guardar resultados en JSON:
   ```bash
   portscanner 192.168.0.39 1 100 -fj
   ```

## Resultados

### Salida en texto
Si usas la opción `-ft`, los resultados se guardan en `scan_results.txt`:
```
Resultados del escaneo de 192.168.0.39 (puertos 1-100):
Puerto 22 abierto
Puerto 80 abierto
```

### Salida en JSON
Si usas la opción `-fj`, los resultados se guardan en `scan_results.json`:
```json
{
    "ip": "192.168.0.39",
    "start_port": 1,
    "end_port": 100,
    "open_ports": [22, 80]
}
```

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas o mejoras, siéntete libre de abrir un issue o enviar un pull request.

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).
