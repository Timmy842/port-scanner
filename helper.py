def show_help():
    help_text = """
Port Scanner - Herramienta para escanear puertos abiertos.

Uso:
  portscanner <IP> <puerto_inicial> <puerto_final>
  portscanner -h | --help

Argumentos:
  <IP>              Dirección IP objetivo (obligatorio)
  <puerto_inicial>  Primer puerto a escanear (obligatorio)
  <puerto_final>    Último puerto a escanear (obligatorio)

Opciones:
  -h, --help        Muestra esta ayuda y termina.

Ejemplo:
  portscanner 192.168.1.1 1 1000
"""
    print(help_text)
