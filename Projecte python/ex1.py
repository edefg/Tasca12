import random

def gllistaaleatoris():
    # Esta función genera una lista de tres números aleatorios entre 1 y 9.
    l = []  # Inicializa una lista vacía.
    for i in range(3):  # Bucle que se repite 3 veces.
        l.append(random.randint(1, 9))  # Añade un número aleatorio entre 1 y 9 a la lista.
    return l  # Devuelve la lista generada.

def llegir_llista():
    # Esta función lee tres números ingresados por el usuario y los guarda en una lista.
    l = []  # Inicializa una lista vacía.
    for i in range(3):  # Bucle que se repite 3 veces.
        l.append(int(input("Introdueixi el número: ")))  # Solicita al usuario un número y lo añade a la lista.
    return l  # Devuelve la lista con los números ingresados por el usuario.

def comparar(l, m):
    # Esta función compara dos listas y proporciona retroalimentación sobre las coincidencias.
    a = [0, 0, 0]  # Inicializa una lista con tres ceros para almacenar los resultados de la comparación.
    for i in range(3):  # Bucle que se repite 3 veces.
        if l[i] == m[i]:  # Compara los elementos de las listas en la misma posición.
            a[i] = 10  # Si son iguales, asigna 10 a la posición correspondiente en la lista 'a'.
    if a[0] == 10 and a[1] == 10 and a[2] == 10:
        # Si todos los elementos son correctos, imprime un mensaje de felicitación y retorna 0.
        print("Enhorabona, ho has encertat tot!")
        return 0
    for i in range(3):  # Bucle que se repite 3 veces.
        if a[i] == 0:
            if m[i] in l:  # Verifica si el elemento existe en la lista original.
                a[i] = 5  # Si existe pero no está en la misma posición, asigna 5 a la posición correspondiente en 'a'.
    for i in range(3):  # Bucle que se repite 3 veces para proporcionar retroalimentación.
        if a[i] == 10:
            print("L'element {} és correcte".format(m[i]))  # Indica que el elemento está en la posición correcta.
        elif a[i] == 5:
            print("L'element {} existeix, però no està al seu lloc".format(m[i]))  # Indica que el elemento existe pero está en otra posición.
        else:
            print("L'element {} no existeix".format(m[i]))  # Indica que el elemento no existe en la lista.

def pex1():
    # Función principal que coordina el juego.
    op = 1  # Inicializa la variable 'op' con un valor distinto de 0 para entrar en el bucle.
    l = gllistaaleatoris()  # Genera la lista de números aleatorios.
    while op != 0:  # Bucle que se repite mientras 'op' no sea 0.
        m = llegir_llista()  # Lee la lista ingresada por el usuario.
        op = comparar(l, m)  # Compara las listas y actualiza 'op' según el resultado de la comparación.
