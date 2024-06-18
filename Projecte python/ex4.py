def main():
    class Videojoc:
        def __init__(self, titol, any_lanzament):
            # Constructor que inicializa los atributos 'titol' y 'any_lanzament' de un videojuego.
            self.titol = titol
            self.any_lanzament = any_lanzament

        def mostrar_informacio(self):
            # Método que imprime la información del videojuego.
            print(f"Títol: {self.titol}")
            print(f"Any de llançament: {self.any_lanzament}")

    class PlayStation(Videojoc):
        def __init__(self, titol, any_lanzament, model):
            # Constructor que inicializa los atributos de un videojuego de PlayStation.
            super().__init__(titol, any_lanzament)
            self.model = model

        def mostrar_informacio(self):
            # Método que imprime la información del videojuego de PlayStation.
            super().mostrar_informacio()
            print(f"Model de PlayStation: {self.model}")

    class Xbox(Videojoc):
        def __init__(self, titol, any_lanzament, model):
            # Constructor que inicializa los atributos de un videojuego de Xbox.
            super().__init__(titol, any_lanzament)
            self.model = model

        def mostrar_informacio(self):
            # Método que imprime la información del videojuego de Xbox.
            super().mostrar_informacio()
            print(f"Model de Xbox: {self.model}")

    class NintendoSwitch(Videojoc):
        def __init__(self, titol, any_lanzament, edicio):
            # Constructor que inicializa los atributos de un videojuego de Nintendo Switch.
            super().__init__(titol, any_lanzament)
            self.edicio = edicio

        def mostrar_informacio(self):
            # Método que imprime la información del videojuego de Nintendo Switch.
            super().mostrar_informacio()
            print(f"Edició de Nintendo Switch: {self.edicio}")

    class BibliotecaVideojocs:
        def __init__(self):
            # Constructor que inicializa una lista vacía para almacenar videojuegos.
            self.videojocs = []

        def afegir_videojoc(self, videojoc):
            # Método que añade un videojuego a la lista.
            self.videojocs.append(videojoc)

        def llistar_videojocs(self):
            # Método que lista e imprime la información de todos los videojuegos en la biblioteca.
            for videojoc in self.videojocs:
                videojoc.mostrar_informacio()
                print("-" * 20)

        # Punto de entrada del programa.
    biblioteca = BibliotecaVideojocs()  # Crea una instancia de BibliotecaVideojocs.

        # Crea instancias de videojuegos específicos.
    joc_ps = PlayStation("The Last of Us Part II", 2020, "PlayStation 4")
    joc_xbox = Xbox("Halo Infinite", 2021, "Xbox Series X")
    joc_switch = NintendoSwitch("The Legend of Zelda: Breath of the Wild", 2017, "Standard Edition")

        # Añade los videojuegos a la biblioteca.
    biblioteca.afegir_videojoc(joc_ps)
    biblioteca.afegir_videojoc(joc_xbox)
    biblioteca.afegir_videojoc(joc_switch)

        # Lista e imprime la información de todos los videojuegos en la biblioteca.
    biblioteca.llistar_videojocs()

def pex4():
    main()