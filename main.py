from cli import run_cli_interface
from gui import GUI

def main_menu():
    print("Seleccione el modo de operación:")
    print("1. Interfaz gráfica (GTK)")
    print("2. Interfaz de línea de comandos (CLI)")

    choice = input("Ingrese el número de su elección: ")

    if choice == "1":
        gui = GUI()
        gui.run()
    elif choice == "2":
        run_cli_interface()
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        main_menu()

if __name__ == "__main__":
    main_menu()
