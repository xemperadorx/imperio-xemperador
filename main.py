ciudadanos = []

def mostrar_comandos():
    print("\nComandos disponibles:")
    print("  crear_ciudadano <nombre>  → Añadir un ciudadano")
    print("  ver_ciudadanos             → Ver todos los ciudadanos")
    print("  expulsar <nombre>          → Expulsar un ciudadano")
    print("  salir                      → Salir del Imperio\n")

print("Bienvenido al Imperio Virtual, XemperadorX 👑")

while True:
    mostrar_comandos()
    comando = input(">> ").strip().split()

    if not comando:
        continue

    accion = comando[0].lower()

    if accion == "crear_ciudadano" and len(comando) == 2:
        nombre = comando[1]
        if nombre not in ciudadanos:
            ciudadanos.append(nombre)
            print(f"{nombre} ha sido añadido al Imperio Virtual.")
        else:
            print(f"{nombre} ya es ciudadano del Imperio.")
    elif accion == "ver_ciudadanos":
        if ciudadanos:
            print("Ciudadanos del Imperio:", ", ".join(ciudadanos))
        else:
            print("Aún no hay ciudadanos en el Imperio.")
    elif accion == "expulsar" and len(comando) == 2:
        nombre = comando[1]
        if nombre in ciudadanos:
            ciudadanos.remove(nombre)
            print(f"{nombre} ha sido expulsado del Imperio.")
        else:
            print(f"{nombre} no existe en el Imperio.")
    elif accion == "salir":
        print("El Imperio Virtual cierra sesión. Hasta la próxima, XemperadorX 👑")
        break
    else:
        print("Comando inválido. Revisa los comandos disponibles.")
