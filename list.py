import random
import string
import time
import threading
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

def generar_cadena():
    caracteres = string.digits + string.ascii_letters
    longitud = random.randint(5, 20)
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def mostrar_nombre_y_descripcion():
    arte_ascii = """
  ██████  ██░ ██  ▄▄▄      ▓█████▄  ▒█████   █     █░    █     █░ ▒█████   ██▀███  ▓█████▄  ██▓     ██▓  ██████ ▄▄▄█████▓
▒██    ▒ ▓██░ ██▒▒████▄    ▒██▀ ██▌▒██▒  ██▒▓█░ █ ░█░   ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌▓██▒    ▓██▒▒██    ▒ ▓  ██▒ ▓▒
░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ░██   █▌▒██░  ██▒▒█░ █ ░█    ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌▒██░    ▒██▒░ ▓██▄   ▒ ▓██░ ▒░
  ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░░█░ █ ░█    ░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌▒██░    ░██░  ▒   ██▒░ ▓██▓ ░ 
▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░▒████▓ ░ ████▓▒░░░██▒██▓    ░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓ ░██████▒░██░▒██████▒▒  ▒██▒ ░ 
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒     ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░ ▒░▓  ░░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   
░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░       ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ ░ ░ ▒  ░ ▒ ░░ ░▒  ░ ░    ░    
░  ░  ░   ░  ░░ ░  ░   ▒    ░ ░  ░ ░ ░ ░ ▒    ░   ░       ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░   ░ ░    ▒ ░░  ░  ░    ░      
      ░   ░  ░  ░      ░  ░   ░        ░ ░      ░           ░        ░ ░     ░        ░        ░  ░ ░        ░           
                            ░                                                       ░                                    
"""
    descripcion = f"{Fore.GREEN}Generador de cadenas aleatorias y escritor en un archivo.{Style.RESET_ALL}"

    print(f"{Fore.MAGENTA}{arte_ascii}{Style.RESET_ALL}")
    print(descripcion)

def mostrar_prompt():
    return f"{Fore.GREEN}sh4dow@root{Fore.BLUE} ~ {Style.RESET_ALL}"

def crear_wordlist():
    ruta_archivo = 'Sh4d0wWordlist.txt'
    try:
        with open(ruta_archivo, 'a') as archivo:
            while True:
                cadena = generar_cadena()
                archivo.write(cadena + '\n')
                print(f"{Fore.MAGENTA}Se generó y agregó al archivo: {cadena}{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\nEsperando 2 segundos...")
        time.sleep(2)

def mostrar_separador(texto):
    separador = "-" * (len(texto) + 8)
    print(f"{Fore.YELLOW}        -{Style.RESET_ALL}{separador}")
    print(f"{Fore.YELLOW}        -{Style.RESET_ALL}   {texto}")
    print(f"{Fore.YELLOW}        -{Style.RESET_ALL}{separador}")

def mostrar_menu():
    menu = """
        [|] Crear la wordlist
        [2] Exit
    """
    print(menu)

def main():
    mostrar_nombre_y_descripcion()
    while True:
        mostrar_menu()
        comando = input(mostrar_prompt())
        if comando.lower() == '1':
            mostrar_separador("Generando Wordlist...")
            thread = threading.Thread(target=crear_wordlist)
            thread.start()
            thread.join()
        elif comando.lower() == 'exit' or comando.lower() == '2':
            print("Saliendo...")
            break
        else:
            print(f"Comando no reconocido: {comando}. Intente de nuevo.")

if __name__ == '__main__':
    main()
