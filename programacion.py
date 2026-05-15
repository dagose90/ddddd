#Adivina el número

def adivinar_numero():
    num= 7
    while True:

        try:
            num = int(input("Introduce un numero: "))
            if num ==7:
                print("Correcto, has acertado")
                break
            print("Intentalo de nuevo")

        except ValueError:
            print("No has introducido ningun numero ")

def clasificar_nota(nota):

    if nota < 0 or nota > 10:
        print("Nota inválida rangos de 0 a 10")
    elif nota <5:
        print(f"Suspenso: {nota}")
    elif nota <7:
        print(f"Aprobado: {nota}")
    elif nota ==9:
        print(f"Notable: {nota}")
    else:
        print(f"Sobresaliente: {nota}")

if __name__ == "__main__":
    clasificar_nota(8.5)
    clasificar_nota(7.5)
    clasificar_nota(3.5)
