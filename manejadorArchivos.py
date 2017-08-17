class Archivo():

    def _init_(self):

        self.archivo

    def abrir(self, nombreArchivo):

        self.archivo = open(nombreArchivo, "a")

    def cerrar(self):

        self.archivo.close()

    def escribir(self, texto):

        self.archivo.write(texto)
    
