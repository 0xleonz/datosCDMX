from ftplib import FTP
import time
import threading
import sys

def intentar_conexion(host, user, passwd, max_reintentos=3, espera=3):
    for intento in range(1, max_reintentos + 1):
        try:
            print(f"Conectando al FTP ({intento}/{max_reintentos})...")
            ftp = FTP(host, timeout=10)
            ftp.login(user=user, passwd=passwd)
            print("Conexión establecida.")
            return ftp
        except Exception as e:
            print(f"Error al conectar: {e}")
            if intento < max_reintentos:
                print(f"Reintentando en {espera} segundos...\n")
                time.sleep(espera)
            else:
                print("No se pudo establecer la conexión.")
                return None

def listar_archivos(ftp):
    print("Archivos disponibles en el servidor:\n")
    archivos = []
    ftp.retrlines("LIST", archivos.append)
    for i, line in enumerate(archivos, 1):
        print(f"{i:2}: {line}")

# animación simple de "descargando..."
def spinner_stop_event():
    return threading.Event()

def spinner(texto, stop_event):
    anim = "|/-\\"
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\r{texto} {anim[i % len(anim)]}")
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * (len(texto) + 2) + "\r")  # limpiar línea

def descargar_archivo(ftp, nombre_archivo):
    stop_event = spinner_stop_event()
    hilo_spinner = threading.Thread(target=spinner, args=(f"Descargando '{nombre_archivo}'", stop_event))
    hilo_spinner.start()
    try:
        with open(nombre_archivo, "wb") as f:
            ftp.retrbinary(f"RETR {nombre_archivo}", f.write)
        stop_event.set()
        hilo_spinner.join()
        print(f"Archivo '{nombre_archivo}' descargado correctamente.")
    except Exception as e:
        stop_event.set()
        hilo_spinner.join()
        print(f"\nNo se pudo descargar el archivo: {e}")

def main():
    host = "sih.conagua.gob.mx"
    user = "presas"
    passwd = "presas"

    ftp = intentar_conexion(host, user, passwd)
    if not ftp:
        return

    listar_archivos(ftp)

    print("\nPor defecto se intentará descargar 'almacenamiento.csv'.")
    respuesta = input("¿Quieres continuar con ese archivo? (s/n): ").strip().lower()

    if respuesta == "s":
        archivo = "almacenamiento.csv"
    else:
        archivo = input("Escribe el nombre exacto del archivo a descargar (o presiona enter para cancelar): ").strip()
        if not archivo:
            print("Descarga cancelada por el usuario.")
            ftp.quit()
            return

    descargar_archivo(ftp, archivo)
    ftp.quit()
    print("Sesión finalizada.")

if __name__ == "__main__":
    main()

