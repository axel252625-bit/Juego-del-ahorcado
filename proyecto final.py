#Proyecto final - Juego del ahorcado
#Materia: Introducción al pensamiento computacional
#Equipo: Axel Peralta Domínguez y José Angel Ramírez Ramírez
#Fecha de entrega: 10/12/2025
#Descripción: Este programa implementa el juego del ahorcado para un solo jugador. Incluye niveles de dificultad, selección aleatoria de palabra,
#búsqueda lineal y una representación gráfica básica del ahorcado.
import random
while True:
# ------------------------Algoritmo de ORDENAMIENTO BURBUJA --------------------------
 def intercambio_burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

 palabras_facil = ["sol","luna","java","casa","flor"]
 palabras_medio = ["pantalla","python","teclado","facultad","palabra"]
 palabras_dificil = ["hexadecimal","binario","definicion","programacion","estadistica"]

 palabras_facil = intercambio_burbuja(palabras_facil)
 palabras_medio = intercambio_burbuja(palabras_medio)
 palabras_dificil = intercambio_burbuja(palabras_dificil)

#------------------------Elegir Dificultad-----------------------------------------------
 dificultad = input("Elige dificultad (facil, medio, dificil): ").lower()

 def seleccionar_palabra(dificultad):
    if dificultad == "facil":
        return random.choice(palabras_facil)
    elif dificultad == "medio":
        return random.choice(palabras_medio)
    else:
        return random.choice(palabras_dificil)


#-------------------------Convertir palabra a "-"-----------------------------------
 def crear_guion(palabra_elegida):
    return ["_"] * len(palabra_elegida)

 palabra_elegida = seleccionar_palabra(dificultad)
 progreso = crear_guion(palabra_elegida)

 def mostrar_progreso(progreso):
    print(" ".join(progreso))

 mostrar_progreso(progreso)

#-----------------------------Pedir letras-------------------------------------------
 def pedir_letra():
    letra = input("Ingresa una letra: ").lower()
    return letra

 def verificar_letra(palabra, progreso, letra):
    for i in range(len(palabra)):
        if palabra[i] == letra:
            progreso[i] = letra
    return progreso

#------------------------------------Dibujo del ahorcado------------------------------
 def mostrar_ahorcado(intentos):
    etapas = [
        """
           ----- 
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        """,
        """
           ----- 
           |   |
           |   O
           |  /|\\
           |  /
           |
        """,
        """
           ----- 
           |   |
           |   O
           |  /|\\
           |
           |
        """,
        """
           ----- 
           |   |
           |   O
           |  /|
           |
           |
        """,
        """
           ----- 
           |   |
           |   O
           |
           |
           |
        """,
        """
           ----- 
           |   |
           |
           |
           |
           |
        """,
        """
           ----- 
           |
           |
           |
           |
           |
        """
    ]
    print(etapas[intentos])

#---------------------Errores y fin del juego--------------------------------
 intentos = 6

 # ← AGREGADO AQUI
 letras_usadas = []

 while "_" in progreso and intentos > 0:
    mostrar_ahorcado(intentos)
    mostrar_progreso(progreso)

    letra = pedir_letra()

    # ← AGREGADO AQUI
    if letra in letras_usadas:
        print("Letra repetida, intenta otra vez.\n")
        continue
    else:
        letras_usadas.append(letra)

    if letra not in palabra_elegida:
        intentos -= 1
        print(f"Letra incorrecta. Te quedan {intentos} intentos.\n")
    else:
        verificar_letra(palabra_elegida, progreso, letra)
        print("Correcto\n")

 if intentos == 0:
    mostrar_ahorcado(intentos)
    print(f"Perdiste. La palabra era: {palabra_elegida}")
 else:
    print("Ganaste. La palabra era:", palabra_elegida)

#------------------------Opcion de volver a jugar------------------------
 volver = input("¿Quieres volver a jugar? si/no: ").lower()
 if volver != "si":
  print ("Juego terminado.")
  break

