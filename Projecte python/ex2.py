import json
import os

def mainprincipal():

    class GestorAgenda:
        def __init__(self, fitxer):
            # Constructor que inicializa la clase con el nombre del archivo donde se guardará la agenda.
            self.fitxer = fitxer
            if not os.path.exists(self.fitxer):
                # Si el archivo no existe, lo crea con una lista vacía.
                with open(self.fitxer, 'w') as f:
                    json.dump([], f)
        
        def _llegir_fitxer(self):
            # Método privado que lee el contenido del archivo JSON y lo devuelve.
            with open(self.fitxer, 'r') as f:
                return json.load(f)
        
        def _escriure_fitxer(self, contingut):
            # Método privado que escribe el contenido proporcionado en el archivo JSON.
            with open(self.fitxer, 'w') as f:
                json.dump(contingut, f, indent=4)
        
        def afegir_element(self, element):
            # Método que añade un elemento a la agenda.
            contingut = self._llegir_fitxer()  # Lee el contenido actual del archivo.
            contingut.append(element)  # Añade el nuevo elemento.
            self._escriure_fitxer(contingut)  # Escribe el nuevo contenido en el archivo.
        
        def recuperar_llista(self):
            # Método que recupera y devuelve la lista completa de elementos de la agenda.
            return self._llegir_fitxer()
        
        def actualitzar_element(self, index, nou_element):
            # Método que actualiza un elemento en una posición específica de la agenda.
            contingut = self._llegir_fitxer()  # Lee el contenido actual del archivo.
            if 0 <= index < len(contingut):
                # Si el índice es válido, actualiza el elemento.
                contingut[index] = nou_element
                self._escriure_fitxer(contingut)  # Escribe el nuevo contenido en el archivo.
            else:
                print("Index fora de rang")  # Muestra un mensaje de error si el índice no es válido.
        
        def esborrar_element(self, index):
            # Método que borra un elemento en una posición específica de la agenda.
            contingut = self._llegir_fitxer()  # Lee el contenido actual del archivo.
            if 0 <= index < len(contingut):
                # Si el índice es válido, borra el elemento.
                del contingut[index]
                self._escriure_fitxer(contingut)  # Escribe el nuevo contenido en el archivo.
            else:
                print("Index fora de rang")  # Muestra un mensaje de error si el índice no es válido.

    def mostrar_menu():
        # Función que muestra el menú de opciones al usuario.
        print("\nMenu de l'Agenda:")
        print("1. Afegir un element")
        print("2. Recuperar llista")
        print("3. Actualitzar un element")
        print("4. Esborrar un element")
        print("5. Sortir")

    def main():
        # Función principal que gestiona la interacción con el usuario.
        agenda = GestorAgenda('agenda.json')  # Crea una instancia de GestorAgenda con el archivo 'agenda.json'.

        while True:
            mostrar_menu()  # Muestra el menú de opciones.
            opcio = input("Selecciona una opció: ")  # Solicita al usuario que seleccione una opción.

            if opcio == '1':
                # Opción para añadir un nuevo elemento a la agenda.
                element = input("Introdueix l'element a afegir: ")
                agenda.afegir_element(element)
            elif opcio == '2':
                # Opción para recuperar y mostrar la lista completa de elementos.
                llista = agenda.recuperar_llista()
                print("Llista actual:")
                for i, element in enumerate(llista):
                    print(f"{i}. {element}")
            elif opcio == '3':
                # Opción para actualizar un elemento en una posición específica.
                index = int(input("Introdueix l'índex de l'element a actualitzar: "))
                nou_element = input("Introdueix el nou element: ")
                agenda.actualitzar_element(index, nou_element)
            elif opcio == '4':
                # Opción para borrar un elemento en una posición específica.
                index = int(input("Introdueix l'índex de l'element a esborrar: "))
                agenda.esborrar_element(index)
            elif opcio == '5':
                # Opción para salir del programa.
                print("Sortint...")
                break
            else:
                print("Opció no vàlida, intenta-ho de nou.")  # Mensaje de error para una opción no válida.


def pex2():
    # Función de prueba simple que imprime un mensaje.
    mainprincipal()