


#POO
class Instrumento:
    def __init__(self, nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    def describir(self):
        print(f"Nombre: {self.nombre}, Tipo: {self.tipo}")

class Alumno:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        print(f"Me llamo: {self.nombre}, Edad: {self.edad}")

class Academia:
    def __init__(self,nombre):
        self.nombre = nombre
        self.alumno = []

    def matricular(self,alumno):
        self.alumno.append(alumno)
    def mostrar_alumnos(self):
        for alumno in self.alumno:
            print(f"Alumno: {alumno.nombre}")

i1=Instrumento("Violin","Cuerda")
a1=Alumno("Pedro","24")
a2=Alumno("Paco","24")
ac1=Academia("Pública")
ac1.matricular(a1)
ac1.matricular(a2)
ac1.mostrar_alumnos()



